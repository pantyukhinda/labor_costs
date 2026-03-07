from datetime import datetime, timedelta, timezone
from typing import Annotated
from pydantic import EmailStr

import jwt
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jwt.exceptions import InvalidTokenError
from pwdlib import PasswordHash

from users.dao import UserDAO
from core.config import settings
from .schemas import Token, TokenData, User
from users.schemas import UserResponse


ACCESS_TOKEN_EXPIRE_MINUTES = 30
OAUTH2_SCHEME = OAuth2PasswordBearer(tokenUrl="token")


class AuthVerifier:
    """Password hashing and verification"""

    def __init__(self):
        self.password_hash = PasswordHash.recommended()
        self.DUMMY_HASH = self.password_hash.hash("dummypassword")

    def verify_password(self, plain_password, hashed_password):
        """Verify a password against a hashed password"""
        return self.password_hash.verify(plain_password, hashed_password)

    def get_password_hash(self, password):
        """Get a hashed password"""
        return self.password_hash.hash(password)

    def create_access_token(self, data: dict, expires_delta: timedelta | None = None):
        """Create a JWT access token"""
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.now(timezone.utc) + expires_delta
        else:
            expire = datetime.now(timezone.utc) + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(
            payload=to_encode,
            key=settings.auth.key,
            algorithm=settings.auth.algorithm,
        )
        return encoded_jwt

    async def get_user(
        self,
        email: EmailStr | None = None,
        user_id: int | None = None,
    ):
        if email:
            user = await UserDAO.find_one_or_none(email=email)
            return user
        if user_id:
            user = await UserDAO.find_one_or_none(id=user_id)
            return user
        return None

    async def authenticate_user(self, email: EmailStr, password: str):
        user = await self.get_user(email=email)
        if not user:
            self.verify_password(password, self.DUMMY_HASH)
            return False
        if not self.verify_password(password, user.password):
            return False
        return user

    async def get_current_user(
        self,
        token: Annotated[str, Depends(OAUTH2_SCHEME)],
    ):
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            payload = jwt.decode(
                jwt=token,
                key=settings.auth.key,
                algorithms=[settings.auth.algorithm],
            )
            user_id = payload.get("user_id")
            if user_id is None:
                raise credentials_exception
            token_data = TokenData(user_id=user_id)
        except InvalidTokenError:
            raise credentials_exception
        user = await self.get_user(user_id=token_data.user_id)
        if user is None:
            raise credentials_exception
        return user


auth_verifier = AuthVerifier()

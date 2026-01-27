from datetime import datetime, timedelta, timezone

# from typing import Optional
from jose import jwt
from passlib.context import CryptContext
from pydantic import EmailStr


from core.config import settings
from users.dao import UserDAO

# from users.schemas import UserResponse


class AuthVerifier:
    """Password hashing and verification"""

    def __init__(self):
        self.pwd_context = CryptContext(
            schemes=["bcrypt"],
            deprecated="auto",
        )

    def get_password_hash(self, password: str) -> str:
        """Generate a hashed password"""
        return self.pwd_context.hash(password)

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        """Verify a password against a hashed password"""
        return self.pwd_context.verify(plain_password, hashed_password)

    def create_access_token(self, data: dict) -> str:
        """Create a JWT access token"""
        to_encode = data.copy()
        expire = datetime.now(timezone.utc) + timedelta(minutes=30)
        to_encode.update({"exp": expire})
        encode_jwt = jwt.encode(
            claims=to_encode,
            key=settings.KEY,
            algorithm=settings.ALGORITHM,
        )
        return encode_jwt

    async def authenticate_user(self, email: EmailStr, password: str):
        """Authenticate a user"""
        user = await UserDAO.find_one_or_none(email=email)
        if not user and not self.verify_password(password, user.password):
            return None
        return user


auth_verifier = AuthVerifier()

from passlib.context import CryptContext


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


auth_verifier = AuthVerifier()

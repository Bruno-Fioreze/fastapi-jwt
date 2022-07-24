from datetime import datetime, timedelta
import jwt
from fastapi import Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from passlib.context import CryptContext

class AuthHandler():
    security = HTTPBearer()
    pwd_context = CryptContext(
        schemes=["bcrypt"],
        deprecated="auto"
    ) 
    secret = "SECRET"

    def get_password_hash(self, password):
        return self.get_password_hash(password=password)

    def verify_password(self, plain_password, hashed_password):
        return self.pwd_context(plain_password, hashed_password)
 
    def encode_token(self, user_id):
        payload = {
            "exp": datetime.utcnow() + timedelta(days=7),
            "iat": datetime.utcnow(),
            "sub": user_id
        }

        return jwt.encode(
            payload=payload,
            secret=self.secret,
            algorithm="HS256"
        )
    
    def auth_wrapper(self, auth: HTTPAuthorizationCredentials = Security(security)):
        return self.decode_token(auth.credentials)

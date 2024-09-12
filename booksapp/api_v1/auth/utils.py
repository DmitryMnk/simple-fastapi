from datetime import timedelta, datetime
import  jwt

from api_v1.users.schemas import UserSchema
from core.config import settings
import bcrypt

TOKEN_TYPE_FIELD = 'token_type'
ACCESS_TOKEN_TYPE = 'access'
REFRESH_TOKEN_TYPE = 'refresh'

def encode_jwt(
    payload: dict,
    private_key:str = settings.PRIVATE_KEY,
    algorithm: str = settings.algorithm,
    expire_minutes: int = settings.access_token_expire_minutes,
    expire_timedelta: timedelta | None = None,

):
    to_encode = payload.copy()
    now: datetime = datetime.now()
    if expire_timedelta:
        print(payload)
        expire = now + expire_timedelta
    else:
        expire = now + timedelta(minutes=expire_minutes)
    to_encode.update({
        'exp': expire,
        'iat': now,
    })
    encoded = jwt.encode(
        to_encode,
        private_key,
        algorithm=algorithm
    )
    return encoded


def decode_jwt(
        token: str | bytes,
        public_key: str = settings.PUBLIC_KEY,
        algorithm:str = settings.algorithm,
):
    decoded = jwt.decode(token, public_key, algorithms=[algorithm])
    return decoded


def hash_password(
    password: str,
) -> bytes:
    salt = bcrypt.gensalt()
    pwd_bytes: bytes = password.encode()
    return bcrypt.hashpw(pwd_bytes, salt)


def validate_password(
        password: str,
        hashed_password: bytes
) -> bool:
    return bcrypt.checkpw(
        password.encode(),
        hashed_password=hashed_password,
    )

def create_jwt(
        token_type: str,
        token_data: dict,
        expire_minutes: int = settings.access_token_expire_minutes,
        expire_timedelta: timedelta | None = None,
):
    jwt_payload = {TOKEN_TYPE_FIELD: token_type}
    jwt_payload.update(token_data)
    return encode_jwt(
        payload=jwt_payload,
        expire_minutes=expire_minutes,
        expire_timedelta=expire_timedelta
    )

def create_access_token(user: UserSchema):
    jwt_payload = {
        'sub': user.username,
        'username': user.username,
        'email': user.email
    }

    return create_jwt(
        token_type=ACCESS_TOKEN_TYPE,
        token_data=jwt_payload,
        expire_minutes=settings.access_token_expire_minutes
    )

def create_refresh_token(user: UserSchema):
    jwt_payload = {
        'sub': user.username,
        'username': user.username,
        'email': user.email
    }

    return create_jwt(
        token_type=REFRESH_TOKEN_TYPE,
        token_data=jwt_payload,
        expire_timedelta=timedelta(days=settings.refresh_token_expire_days),
    )
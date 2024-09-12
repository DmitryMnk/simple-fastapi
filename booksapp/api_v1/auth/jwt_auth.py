from fastapi import APIRouter, Depends, Form, status, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials, OAuth2PasswordBearer
from jwt import InvalidTokenError

from pydantic import BaseModel
from api_v1.users.schemas import UserSchema
from api_v1.auth.utils import hash_password, encode_jwt, validate_password, decode_jwt, create_access_token, \
    TOKEN_TYPE_FIELD, ACCESS_TOKEN_TYPE, REFRESH_TOKEN_TYPE


http_bearer = HTTPBearer()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/api/v1/jwt/login')


class TokenInfo(BaseModel):
    access_token: str
    refresh_token: str | None = None
    token_type: str = 'Bearer'


router = APIRouter(prefix='/jwt', tags=['JWT'])


john = UserSchema(
    username='john',
    password=hash_password('qwerty'),
    email='john@example.com'
)


sam = UserSchema(
    username='sam',
    password=hash_password('secret'),
)


users_db: dict[str, UserSchema] = {
    john.username: john,
    sam.username: sam
}


def validate_token_type(
    payload: dict,
    token_type: str,
) -> bool:
    if payload.get(TOKEN_TYPE_FIELD) == token_type:
        return True
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED
    )


def validate_user(
    username: str = Form(),
    password: str = Form(),
):
    unauth_exc = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='invalid username or password'
    )

    if not (user := users_db.get(username)):
        raise unauth_exc

    if not user.active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='user_inactive'
        )

    if validate_password(password, user.password):
        return user

    raise unauth_exc


def get_current_token_payload(
        token: str = Depends(oauth2_scheme)
) -> UserSchema:

    try:
        payload = decode_jwt(
            token=token
        )
    except InvalidTokenError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f'invalid token error',
        )
    return payload


def get_user_by_token_sub(payload: dict) -> UserSchema:

    username: str | None = payload.get('sub')
    if user := users_db.get(username):
        return user
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='token_invalid (user_not_found)'
    )


def get_current_auth_user(
    token_type: str,
    payload: dict = Depends(get_current_token_payload),
) -> UserSchema:
    validate_token_type(payload, token_type)
    user = get_user_by_token_sub(payload)
    return user

def get_auth_user_from_token_of_type(token_type: str):
    def get_auth_user_from_token(
            payload: dict = Depends(get_current_token_payload)
    ) -> UserSchema:
        validate_token_type(payload, token_type)
        return get_user_by_token_sub(payload)

    return get_auth_user_from_token

def get_current_active_user(
    user: UserSchema = Depends(get_current_auth_user)
):
    if user.active:
        return user
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail='user inactive'
    )



@router.post('/login', response_model=TokenInfo)
def login(
    user: UserSchema = Depends(validate_user)
):
    jwt_payload = {
        'subject': user.username,
        'username': user.username,
        'email': user.email
    }
    access_token = create_access_token(user)
    refresh_token = create_access_token(user)
    return TokenInfo(
        access_token=access_token,
        refresh_token=refresh_token,
    )


@router.post('/refresh', response_model=TokenInfo, response_model_exclude_none=True)
def auth_refresh_jwt():
    pass


@router.get('/users/me')
def auth_user_check_self(
    user: UserSchema = Depends(get_current_active_user)
):
    return {
        'username': user.username,
        'email': user.email
    }

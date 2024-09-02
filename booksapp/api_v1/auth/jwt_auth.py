from fastapi import APIRouter, Depends, Form, status, HTTPException


from  pydantic import BaseModel
from api_v1.users.schemas import UserSchema
from api_v1.auth.utils import hash_password, encode_jwt, validate_password

class TokenInfo(BaseModel):
    access_token: str
    token_type: str


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


@router.post('/login')
def login(
    user: UserSchema = Depends(validate_user)
):
    jwt_payload = {
        'subject': user.username,
        'username': user.username,
        'email': user.email
    }
    token = encode_jwt(jwt_payload)
    return TokenInfo(
        access_token=token,
        token_type='Bearer'
    )
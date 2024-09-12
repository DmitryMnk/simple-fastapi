from fastapi_users.authentication import AuthenticationBackend, BearerTransport, JWTStrategy

from core.authentication.transport import bearer_transport
from core.config import settings
from core.authentication.transport import bearer_transport
from .strategy import get_database_strategy

auth_backend = AuthenticationBackend(
    name='access-tokens-db',
    transport=bearer_transport,
    get_strategy=get_database_strategy
)
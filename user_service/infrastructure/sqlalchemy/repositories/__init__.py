from user_service.domain.repositories.database.user_repository import UserRepository
from user_service.infrastructure.sqlalchemy.database import Database
from user_service.infrastructure.sqlalchemy.repositories.user_repository_impl import (
    UserRepositoryImpl,
)


def create_user_repository(database: Database) -> UserRepository:
    return UserRepositoryImpl(database._session_factory)

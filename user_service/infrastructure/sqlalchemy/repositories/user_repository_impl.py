from typing import List, Optional

from user_service.domain.entities.user_entity import UserEntity
from user_service.domain.repositories.database.user_repository import UserRepository
from user_service.infrastructure.sqlalchemy.database import SessionFactory
from user_service.infrastructure.sqlalchemy.models.user import User


class UserRepositoryImpl(UserRepository):
    def __init__(self, session_factory: SessionFactory) -> None:
        self.session_factory = session_factory

    def save(self, entity: UserEntity) -> UserEntity:
        with self.session_factory() as session:
            user = User(name=entity.name)
            session.add(user)
            session.commit()
            session.refresh(user)
            return UserEntity(id=user.id, name=user.name)

    def get_by_id(self, id: int) -> Optional[UserEntity]:
        with self.session_factory() as session:
            model = session.query(User).filter(User.id == id).first()
            return UserEntity(id=model.id, name=model.name)

    def find_by_id(self, id: int) -> List[UserEntity]:
        with self.session_factory() as session:
            result = session.query(User).filter(User.id == id).all()
            return list(UserEntity(id=model.id, name=model.name) for model in result)

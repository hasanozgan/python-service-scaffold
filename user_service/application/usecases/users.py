from typing import List

from user_service.domain.entities.user_entity import UserEntity
from user_service.domain.repositories.database.user_repository import UserRepository


class UserUseCases:
    """
    user use cases
    """

    repository: UserRepository

    def __init__(self, repository: UserRepository) -> None:
        self.repository = repository

    def get_users(self, id: int) -> List[UserEntity]:
        return self.repository.find_by_id(id)

    def create_user(self, name: str) -> int:
        userEntity = UserEntity(id=-1, name=name)
        newUserEntity = self.repository.save(userEntity)
        return newUserEntity.id

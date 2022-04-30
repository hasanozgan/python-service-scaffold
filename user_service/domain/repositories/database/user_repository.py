from typing import List, Optional, Protocol

from user_service.domain.entities.user_entity import UserEntity


class UserRepository(Protocol):
    def save(self, entity: UserEntity) -> UserEntity:
        ...

    def find_by_id(self, id: int) -> Optional[UserEntity]:
        ...

    def find_all(self) -> List[UserEntity]:
        ...

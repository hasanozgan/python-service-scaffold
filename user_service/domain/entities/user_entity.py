from dataclasses import dataclass


@dataclass(frozen=True)
class UserEntity:
    id: int
    name: str

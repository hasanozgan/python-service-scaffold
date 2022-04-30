import strawberry


@strawberry.type
class UserResponse:
    name: str

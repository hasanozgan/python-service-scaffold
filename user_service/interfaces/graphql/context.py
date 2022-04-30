from dataclasses import dataclass

from user_service.application.usecases.users import UserUseCases


@dataclass
class GraphQLContext:
    user_usecases: UserUseCases

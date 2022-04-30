from fastapi import FastAPI

from user_service.application.usecases.users import UserUseCases
from user_service.infrastructure.settings import current_settings
from user_service.infrastructure.sqlalchemy.database import Database
from user_service.infrastructure.sqlalchemy.repositories import create_user_repository
from user_service.interfaces.graphql.context import GraphQLContext
from user_service.interfaces.graphql.graphql import GraphQL




def __create_graphql_context() -> GraphQLContext:
    db = Database(current_settings.pg_dsn)
    return GraphQLContext(
        user_usecases=UserUseCases(repository=create_user_repository(db))
    )



app = FastAPI()
app.add_route("/graphql", GraphQL(__create_graphql_context()))



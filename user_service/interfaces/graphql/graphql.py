from abc import ABC
from typing import Union

import strawberry
from strawberry.asgi import GraphQL as BaseGraphQL
from strawberry.asgi import Request, Response, WebSocket
from strawberry.extensions.tracing import OpenTelemetryExtension

from user_service.interfaces.graphql.context import GraphQLContext
from user_service.interfaces.graphql.schema.mutation import Mutation
from user_service.interfaces.graphql.schema.query import Query

schema = strawberry.Schema(Query, Mutation, extensions=[OpenTelemetryExtension])


class GraphQL(BaseGraphQL, ABC):
    schema: strawberry.Schema
    context: GraphQLContext

    def __init__(self, context: GraphQLContext) -> None:
        super().__init__(schema)
        self.context = context

    async def get_context(
        self, request: Union[Request, WebSocket], response: Response
    ) -> GraphQLContext:
        return self.context

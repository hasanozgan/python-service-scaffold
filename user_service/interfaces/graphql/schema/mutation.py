from typing import Any

import strawberry
from strawberry.types import Info

from user_service.interfaces.graphql.context import GraphQLContext
from user_service.interfaces.graphql.permissions import PermissionActions, required


@strawberry.type
class Mutation:
    @strawberry.field
    @required(action=PermissionActions.PUT, module="user", operation="create_user")
    async def create_user(self, info: Info[GraphQLContext, Any], name: str) -> int:
        return info.context.user_usecases.create_user(name)

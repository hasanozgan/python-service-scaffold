from typing import Any, List

import strawberry
from strawberry.types import Info

from user_service.interfaces.graphql.context import GraphQLContext
from user_service.interfaces.graphql.permissions import PermissionActions, required
from user_service.interfaces.graphql.schema.responses import UserResponse


@strawberry.type
class Query:
    @strawberry.field
    @required(action=PermissionActions.GET, module="user", operation="get_users")
    def users(
        self, info: Info[GraphQLContext, Any], id: strawberry.ID
    ) -> List[UserResponse]:
        return list(
            map(
                lambda entity: UserResponse(name=entity.name),
                info.context.user_usecases.get_users(int(id)),
            )
        )

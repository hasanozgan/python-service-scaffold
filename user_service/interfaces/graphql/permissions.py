import logging
from enum import Enum
from functools import wraps
from typing import Any, Callable, TypeVar, cast

AuthorisedFunc = TypeVar("AuthorisedFunc", bound=Callable[..., Any])

logger = logging.getLogger(__name__)


class UnauthorisedError(Exception):
    pass


class InvalidPermissionNameError(Exception):
    pass


class PermissionActions(Enum):
    GET = "get"
    PUT = "put"
    DELETE = "delete"

    def __str__(self) -> str:
        return self.value


logger = logging.getLogger(__name__)


def required(
    action: PermissionActions, module: str = "", operation: str = ""
) -> Callable[[AuthorisedFunc], AuthorisedFunc]:
    def decorator(service_func: AuthorisedFunc) -> AuthorisedFunc:
        @wraps(service_func)
        def has_permission(*args: Any, **kwargs: Any) -> Any:
            logger.warning(
                "Authorisation is not implemented for %s::%s::%s in `required` decorator yet",
                action,
                module,
                operation,
            )
            return service_func(*args, **kwargs)

        return cast(AuthorisedFunc, has_permission)

    return decorator

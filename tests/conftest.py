import pytest
from fastapi.testclient import TestClient
from requests import Response

from user_service.infrastructure.setup import app


class ApiClient(TestClient):
    def __init__(self, app, prefix="", user=None, *args, **kwargs):
        self.user = user
        self.prefix = prefix
        super().__init__(app, *args, **kwargs)

    def get(self, url: str, **kwargs) -> Response:
        return super().get(url, **kwargs)

    def op(self, url: str, json=None, **kwargs) -> Response:
        res = super().post(url, None, json, **kwargs).json()
        if "item" in res:
            return res["item"]
        return res


@pytest.fixture(scope="session")
def ambassador_api_client():
    return ApiClient(app)


@pytest.fixture(scope="session")
def graphql_client():
    return ApiClient(app)

from user_service.application.usecases.users import UserUseCases
from user_service.interfaces.graphql.schema.responses import UserResponse


def test_users(when, graphql_client):
    when(UserUseCases).get_users(1234).thenReturn([UserResponse(name="Test User")])

    query = """
        query TestQuery($id: ID!) {
            users(id: $id) {
                name
            }
        }
    """

    response = graphql_client.post(
        "/graphql",
        json={
            "query": query,
            "variables": {"id": 1234},
        },
    )

    assert response.status_code == 200
    assert response.json() == {"data": {"users": [{"name": "Test User"}]}}

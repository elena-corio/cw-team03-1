import asyncio
from gql import gql, Client
from gql.transport.websockets import WebsocketsTransport

# Implement the adapter logic for subscribing to real-time updates
# from Speckle using GraphQL over WebSocket.

#  Define the GraphQL subscription query for project version updates
SUBSCRIPTION_QUERY = gql("""
    subscription ProjectVersionsUpdated($projectId: String!) {
        projectVersionsUpdated(id: $projectId) {
            id
            modelId
            type
            version {
                id
                message
                createdAt
            }
        }
    }
""")

# Dependency injection for easier testing (transport and client can be mocked)
async def subscribe_project_versions_updated(token, project_id, on_update, transport=None, client=None):
    """
    Subscribe to project version updates and call on_update for each update.
    Optionally accept transport and client for easier testing.
    """
    if transport is None:
        transport = WebsocketsTransport(
            url="wss://app.speckle.systems/graphql",
            init_payload={"Authorization": f"Bearer {token}"}
        )
    if client is None:
        client = Client(transport=transport, fetch_schema_from_transport=False)
    try:
        async with client as session:
            async for result in session.subscribe(
                SUBSCRIPTION_QUERY,
                variable_values={"projectId": project_id}
            ):
                await on_update(result.get("projectVersionsUpdated"))
    finally:
        await transport.close()
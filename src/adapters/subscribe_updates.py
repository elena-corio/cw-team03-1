import os
from dotenv import load_dotenv
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

async def subscribe_project_versions_updated(project_id, on_update, transport=None, client=None):
    """
    Subscribe to project version updates and call on_update for each update.
    Optionally accept transport and client for easier testing.
    """
    # Load environment variables from a local .env file, if present
    load_dotenv()

    # Get token and server host from environment
    token = os.environ.get("SPECKLE_TOKEN")
    if transport is None:
        transport = WebsocketsTransport(
            url="wss://app.speckle.systems/graphql",
            init_payload={"Authorization": f"Bearer {token}"}
        )
    if client is None:
        client = Client(transport=transport, fetch_schema_from_transport=False)
    try:
        async with client as session:
            print("Subscription started, waiting for updates...")
            async for result in session.subscribe(
                SUBSCRIPTION_QUERY,
                variable_values={"projectId": project_id}
            ):
                # Make the subscription code reusable and testable
                print("Received subscription result:", result)
                await on_update(result.get("projectVersionsUpdated"))
    
    finally:
        await transport.close()
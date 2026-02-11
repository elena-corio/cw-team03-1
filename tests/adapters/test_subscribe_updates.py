import pytest
from unittest.mock import AsyncMock
from adapters.subscribe_updates import subscribe_project_versions_updated

# Marks the test as async so pytest can run it as a coroutine.
@pytest.mark.asyncio
async def test_subscribe_project_versions_updated_calls_on_update():
    # Sets up fake data to simulate a real update from the server.
    dummy_update = {"id": "123", "modelId": "abc", "type": "update", "version": {"id": "v1", "message": "msg", "createdAt": "now"}}
    dummy_result = {"projectVersionsUpdated": dummy_update}

    # Defines an async generator that yields the fake result 
    # to simulate the behavior of the subscribe method in the GraphQL client.
    async def fake_subscribe(*args, **kwargs):
        yield dummy_result

    # Creates a mock session object and sets its subscribe method to the fake async generator.
    mock_session = AsyncMock()
    mock_session.subscribe = fake_subscribe

    # Creates a mock client that acts as an async context manager, 
    # returning the mock session when entered.
    mock_client = AsyncMock()
    mock_client.__aenter__.return_value = mock_session

    # Creates a mock transport object and sets its close method to a mock async function.
    mock_transport = AsyncMock()
    mock_transport.close = AsyncMock()

    # Creates a mock on_update callback function.
    on_update = AsyncMock()

    # Calls the function under test, injecting the mocks so no real network calls are made.
    await subscribe_project_versions_updated(
        "project_id", on_update,
        transport=mock_transport, client=mock_client
    )

    # Asserts that the on_update callback was called once with the expected dummy update.
    on_update.assert_awaited_once_with(dummy_update)
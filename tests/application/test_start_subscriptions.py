import pytest
from unittest.mock import AsyncMock, patch
from application import start_subscription

@pytest.mark.asyncio
async def test_start_subscription_calls_subscribe(monkeypatch):
    # Mock the subscribe_project_versions_updated function
    mock_subscribe = AsyncMock()
    monkeypatch.setattr(
        "application.start_subscription.subscribe_project_versions_updated",
        mock_subscribe
    )

    # Run the function
    await start_subscription.start_subscription()

    # Assert the subscription function was called once
    assert mock_subscribe.await_count == 1
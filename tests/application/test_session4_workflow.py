import pytest
from unittest.mock import AsyncMock, patch
from application.session4_workflow import run_backup_updates_workflow

@pytest.mark.asyncio
def test_run_backup_updates_workflow():
    with patch("application.session4_workflow.subscribe_project_versions_updated", new_callable=AsyncMock) as mock_subscribe:
        import asyncio
        asyncio.run(run_backup_updates_workflow())
        assert mock_subscribe.await_count == 1
import pytest
from unittest.mock import Mock
from adapters.query_object_data import query_object_data_graphql

def test_query_object_data_graphql():
    # Create a mock client with a mock httpclient
    mock_httpclient = Mock()
    expected_result = {"project": {"object": {"id": "123", "speckleType": "type", "data": {"foo": "bar"}}}}
    mock_httpclient.execute.return_value = expected_result

    mock_client = Mock()
    mock_client.httpclient = mock_httpclient

    # Call the function
    result = query_object_data_graphql(mock_client, "mock_proj_id", "mock_obj_id")

    # Assert the result is as expected
    assert result == expected_result
    
    # Assert the query was called with correct variables
    _, kwargs = mock_httpclient.execute.call_args
    assert kwargs["variable_values"] == {"projectId": "mock_proj_id", "objectId": "mock_obj_id"}
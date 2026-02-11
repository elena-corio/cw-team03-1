import os
import json
from unittest.mock import Mock

from application import util_export_object_data

def test_export_object_data_creates_json_file():
    # Set up dummy values
    util_export_object_data.PROJECT_ID = "dummy_project"
    util_export_object_data.OBJECT_ID = "dummy_object"
    util_export_object_data.OBJECT_DATA_FILE = "test_object_data.json"
    
    # Save output file in the test directory
    output_file = os.path.abspath("test_object_data.json")
    util_export_object_data.OBJECT_DATA_FILE = output_file

    # Create mock objects
    mock_client = Mock()
    mock_query = Mock(return_value={"project": {"object": {"data": {"foo": "bar"}}}})

    # Inject mocks by replacing the module's functions
    util_export_object_data.get_client = Mock(return_value=mock_client)
    util_export_object_data.query_object_data_graphql = mock_query

    # Run the function
    util_export_object_data.export_object_data()

    # Check that the file was created and contains expected data
    assert os.path.exists(output_file)
    with open(output_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    assert data["projectId"] == "dummy_project"
    assert data["objectId"] == "dummy_object"
    assert data["data"] == {"foo": "bar"}

    # Clean up
    os.remove(output_file)
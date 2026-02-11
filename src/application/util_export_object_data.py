import os
import json
from adapters.get_client import get_client
from adapters.util_query_object_data import query_object_data_graphql
from config import PROJECT_ID, OBJECT_ID, OBJECT_DATA_FILE

def export_object_data():
    """
    Fetch object data and save to JSON file.
    """
    # Authenticate with Speckle
    client = get_client()
    print(f"✓ Authenticated with Speckle")
    
    # Execute GraphQL query
    try:
        graphql_result = query_object_data_graphql(client, PROJECT_ID, OBJECT_ID)
        print(f"✓ GraphQL query executed successfully")
    except Exception as e:
        print(f"⚠ GraphQL query failed: {e}")
        return
    
    # Prepare output data
    output = {
        "projectId": PROJECT_ID,
        "objectId": OBJECT_ID,
        "data": graphql_result["project"]["object"]["data"]
    }
    
    # Save to JSON file in the same directory as this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_file = os.path.join(script_dir, OBJECT_DATA_FILE)
    
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, default=str)
    
    print(f"✓ Saved object data to {output_file}")
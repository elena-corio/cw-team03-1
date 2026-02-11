from gql import gql

# Connect to Speckle's GraphQL API and fetches object data
# from a specified project and object ID

GET_OBJECT_DATA_QUERY = gql("""
query GetObjectDataJSON($objectId: String!, $projectId: String!) {
    project(id: $projectId) {
        object(id: $objectId) {
            id
            speckleType
            data
        }
    }
}
""")

def query_object_data_graphql(client, project_id: str, object_id: str) -> dict:
    """
    Execute GraphQL query using the client's HTTP session
    """
    result = client.httpclient.execute(GET_OBJECT_DATA_QUERY, variable_values={
        "projectId": project_id,
        "objectId": object_id
    })
    return result


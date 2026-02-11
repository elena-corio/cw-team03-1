from gql import gql

# Connect to Speckle's GraphQL API and fetches object data
# from a specified project and object ID

def query_object_data_graphql(client, project_id: str, object_id: str) -> dict:
    #  Query object data from Speckle using GraphQL API.
    query = gql("""
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
    
    variables = {
        "projectId": project_id,
        "objectId": object_id
    }
    
    # Execute GraphQL query using the client's HTTP session
    result = client.httpclient.execute(query, variable_values=variables)
    return result


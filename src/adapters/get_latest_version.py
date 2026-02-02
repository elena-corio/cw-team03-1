from config import PROJECT_ID, SOURCE_MODEL_ID

def get_latest_version(client):
    # Get the latest version
    versions = client.version.get_versions(SOURCE_MODEL_ID, PROJECT_ID, limit=1)
    if not versions.items:
        print("No versions found.")
        return
    
    latest_version = versions.items[0]
    print(f"✓ Fetching version: {latest_version.id}")
    
    return latest_version
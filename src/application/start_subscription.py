import asyncio
from adapters.subscribe_updates import subscribe_project_versions_updated
from config import SPECKLE_TOKEN, PROJECT_ID

# This module defines the logic to start a subscription to Speckle updates and handle incoming data.

async def handle_update(data):
    
    """Callback function to handle incoming updates from the subscription."""
    
    print("=" * 50)
    print("📦 New Update Received!")
    print("=" * 50)
    if data:
        print(f"ID: {data.get('id')}")
        print(f"Model ID: {data.get('modelId')}")
        print(f"Type: {data.get('type')}")
        version = data.get('version')
        if version:
            print(f"\nVersion Details:")
            print(f"  - Version ID: {version.get('id')}")
            print(f"  - Message: {version.get('message')}")
            print(f"  - Created At: {version.get('createdAt')}")
        print("\n")

async def start_subscription():
    
    """Function to start the subscription and handle updates."""
    
    print(f"🔌 Connected to Speckle WebSocket")
    print(f"📡 Listening for updates on project: {PROJECT_ID}")
    print("Press Ctrl+C to stop\n")
    try:
        await subscribe_project_versions_updated(SPECKLE_TOKEN, PROJECT_ID, handle_update)
    except KeyboardInterrupt:
        print("\n\n👋 Subscription stopped by user")
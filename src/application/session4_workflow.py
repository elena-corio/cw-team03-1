import asyncio
import json
from datetime import datetime
from adapters.subscribe_updates import subscribe_project_versions_updated
from config import SPECKLE_TOKEN, PROJECT_ID

async def save_update_to_json(data):
    if data:
        filename = f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Saved update to {filename}")

async def run_backup_updates_workflow():
    print(f"🔌 Connected to Speckle WebSocket")
    print(f"📡 Listening for updates on project: {PROJECT_ID}")
    print("Press Ctrl+C to stop\n")
    try:
        await subscribe_project_versions_updated(SPECKLE_TOKEN, PROJECT_ID, save_update_to_json)
    except KeyboardInterrupt:
        print("\n\n👋 Subscription stopped by user")
    except Exception as e:
        print(f"\n❌ Error: {e}")
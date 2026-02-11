import asyncio
from application.session3_workflow import run_receive_and_send_data_workflow
from application.session4_workflow import run_backup_updates_workflow

async def run_receive_and_send_data_workflow_async():
    run_receive_and_send_data_workflow()

async def main():
    await asyncio.gather(
        run_backup_updates_workflow(),
        run_receive_and_send_data_workflow_async()
    )


if __name__ == "__main__":
    asyncio.run(main())
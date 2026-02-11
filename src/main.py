import asyncio
from application.session4_workflow import run_backup_updates_workflow


def main():
    run_backup_updates_workflow()
    asyncio.run(run_backup_updates_workflow())


if __name__ == "__main__":
    main()
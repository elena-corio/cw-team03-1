import os

WORKSPACE_ID = os.getenv("WORKSPACE_ID", "a1cd06bae2")
PROJECT_ID = os.getenv("PROJECT_ID", "128262a20c")
SOURCE_MODEL = os.getenv("SOURCE_MODEL", "a1014e4b32")
MODEL_NAME = os.getenv("MODEL_NAME", "homework/session03/team_03.1")
MODEL_DESCRIPTION = os.getenv("MODEL_DESCRIPTION", "Model created for CW Team 03.1 Session 03")
OFFSET_Z = float(os.getenv("OFFSET_Z", "16000"))
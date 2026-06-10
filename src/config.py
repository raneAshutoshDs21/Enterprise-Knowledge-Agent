from os import getenv
from dotenv import load_dotenv
from typing import Final, cast

load_dotenv()

PROJECT_ENDPOINT: Final[str] = cast(
    str,
    getenv("PROJECT_ENDPOINT")
)

MODEL_DEPLOYMENT_NAME: Final[str] = cast(
    str,
    getenv("MODEL_DEPLOYMENT_NAME")
)

AGENT_NAME: Final[str] = cast(
    str,
    getenv("AGENT_NAME")
)

if not PROJECT_ENDPOINT:
    raise ValueError("PROJECT_ENDPOINT not found in .env")

if not AGENT_NAME:
    raise ValueError("AGENT_NAME not found in .env")
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

AZURE_CLIENT_ID: Final[str] = cast(
    str,
    getenv("AZURE_CLIENT_ID")
)

AZURE_TENANT_ID: Final[str] = cast(
    str,
    getenv("AZURE_TENANT_ID")
)

AZURE_CLIENT_SECRET: Final[str] = cast(
    str,
    getenv("AZURE_CLIENT_SECRET")
)

APPLICATIONINSIGHTS_CONNECTION_STRING: Final[str] = cast(
    str,
    getenv("APPLICATIONINSIGHTS_CONNECTION_STRING")
)

if not PROJECT_ENDPOINT:
    raise ValueError("PROJECT_ENDPOINT not found in .env")

if not AGENT_NAME:
    raise ValueError("AGENT_NAME not found in .env")

if not AZURE_CLIENT_ID:
    raise ValueError("AZURE_CLIENT_ID not found in .env")

if not AZURE_TENANT_ID:
    raise ValueError("AZURE_TENANT_ID not found in .env")

if not AZURE_CLIENT_SECRET:
    raise ValueError("AZURE_CLIENT_SECRET not found in .env")

if not APPLICATIONINSIGHTS_CONNECTION_STRING:
    raise ValueError("APPLICATIONINSIGHTS_CONNECTION_STRING not found in .env")
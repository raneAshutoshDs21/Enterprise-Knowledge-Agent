from azure.identity import ClientSecretCredential
from azure.ai.projects import AIProjectClient

from src.config import (
    PROJECT_ENDPOINT,
    AZURE_CLIENT_ID,
    AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET,
)


def get_project_client() -> AIProjectClient:
    """
    Create an authenticated Azure AI Foundry project client.
    """

    credential = ClientSecretCredential(
        tenant_id=AZURE_TENANT_ID,
        client_id=AZURE_CLIENT_ID,
        client_secret=AZURE_CLIENT_SECRET,
    )

    client = AIProjectClient(
        endpoint=PROJECT_ENDPOINT,
        credential=credential,
    )

    return client
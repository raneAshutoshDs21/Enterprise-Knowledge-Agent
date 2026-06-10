from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

from src.config import PROJECT_ENDPOINT


def get_project_client() -> AIProjectClient:
    """
    Create an authenticated Azure AI Foundry project client.
    """

    credential = DefaultAzureCredential()

    client = AIProjectClient(
        endpoint=PROJECT_ENDPOINT,
        credential=credential,
    )

    return client
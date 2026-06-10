from src.agent_client import get_project_client
from src.config import MODEL_DEPLOYMENT_NAME


def main():
    project_client = get_project_client()

    openai_client = project_client.get_openai_client()

    response = openai_client.responses.create(
        model=MODEL_DEPLOYMENT_NAME,
        input="What is Azure AI Foundry?"
    )

    print("\nResponse:\n")
    print(response.output_text)


if __name__ == "__main__":
    main()
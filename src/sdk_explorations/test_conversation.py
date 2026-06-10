from src.agent_client import get_project_client


def main():
    print("Connecting to Azure AI Foundry...")

    try:
        project_client = get_project_client()

        openai_client = project_client.get_openai_client()

        print("Creating conversation...")

        conversation = openai_client.conversations.create()

        print("✅ Conversation Created Successfully")
        print(f"Conversation ID: {conversation.id}")

    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    main()
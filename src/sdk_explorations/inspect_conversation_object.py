from src.agent_client import get_project_client


def main():
    project_client = get_project_client()

    openai_client = project_client.get_openai_client()

    conversation = openai_client.conversations.create()

    print(type(conversation))
    print()
    print(conversation)
    print()
    print(dir(conversation))


if __name__ == "__main__":
    main()
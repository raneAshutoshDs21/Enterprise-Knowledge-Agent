from src.agent_client import get_project_client


def main():
    project_client = get_project_client()

    openai_client = project_client.get_openai_client()

    import inspect

    print(inspect.signature(openai_client.responses.create))


if __name__ == "__main__":
    main()
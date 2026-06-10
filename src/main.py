from src.agent_client import get_project_client


def main():
    print("Connecting to Azure AI Foundry...")

    try:
        client = get_project_client()

        print("Connected successfully!")

        print("\nAvailable Agents")
        print("-" * 50)

        agents = client.agents.list()

        count = 0

        for agent in agents:
            count += 1

            print(f"Agent ID: {agent.id}")
            print(f"Name: {agent.name}")
            print("-" * 50)

        print(f"\nTotal Agents Found: {count}")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
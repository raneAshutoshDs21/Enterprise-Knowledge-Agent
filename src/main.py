from src.agent_client import get_project_client


def main():
    print("Connecting to Azure AI Foundry...")

    try:
        client = get_project_client()

        print("✅ Connected successfully!")
        print(f"Client Type: {type(client).__name__}")

        print("\nChecking project access...")

        deployments = list(client.deployments.list())

        print(f"✅ Project accessible")
        print(f"Deployments Found: {len(deployments)}")

        for deployment in deployments:
            print(f"- {deployment.name}")

    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    main()
from src.agent_client import get_project_client

client = get_project_client()

openai_client = client.get_openai_client()

print(type(openai_client))

print("\nMethods:\n")

for item in dir(openai_client):
    if not item.startswith("_"):
        print(item)
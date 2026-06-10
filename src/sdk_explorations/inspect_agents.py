from src.agent_client import get_project_client

client = get_project_client()

print(type(client.agents))
print("\nMethods:\n")

for item in dir(client.agents):
    if not item.startswith("_"):
        print(item)
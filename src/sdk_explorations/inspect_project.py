from src.agent_client import get_project_client

client = get_project_client()

for item in dir(client):
    if not item.startswith("_"):
        print(item)
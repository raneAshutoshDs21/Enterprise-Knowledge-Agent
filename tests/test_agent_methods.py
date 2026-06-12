# tests/test_agent_methods.py

from src.agent_client import get_project_client

client = get_project_client()

print(type(client.agents))

print("\nMethods")
print("-" * 50)

for method in dir(client.agents):
    if not method.startswith("_"):
        print(method)
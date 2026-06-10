from src.agent_client import get_project_client

client = get_project_client()

openai_client = client.get_openai_client()

print("\nCONVERSATIONS")
print("-" * 50)

for item in dir(openai_client.conversations):
    if not item.startswith("_"):
        print(item)

print("\nRESPONSES")
print("-" * 50)

for item in dir(openai_client.responses):
    if not item.startswith("_"):
        print(item)
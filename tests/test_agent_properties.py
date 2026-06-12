from src.services.agent_service import AgentService

service = AgentService()

agent = service.get_agent()

print("\nAGENT KEYS")
print("-" * 50)

for key in agent.keys():
    print(key)
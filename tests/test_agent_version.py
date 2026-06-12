from src.services.agent_service import AgentService

service = AgentService()

agent = service.get_agent()

latest = agent["versions"]["latest"]

print("\nLATEST VERSION")
print("-" * 50)

print(latest)
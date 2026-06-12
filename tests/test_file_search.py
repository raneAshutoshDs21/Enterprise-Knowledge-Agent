from src.services.agent_service import AgentService

service = AgentService()

agent = service.get_agent()

latest = agent["versions"]["latest"]

instructions = latest["definition"]["instructions"]

tools = latest["definition"]["tools"]

print("INSTRUCTIONS")
print("-" * 50)
print(instructions)

print("\nTOOLS")
print("-" * 50)
print(tools)
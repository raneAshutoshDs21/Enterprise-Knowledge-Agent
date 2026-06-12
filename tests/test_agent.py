'''
from src.services.agent_service import AgentService


def main():

    service = AgentService()

    agent = service.get_agent()

    print("Agent Found!")
    print(f"Name: {agent.name}")
    print(f"ID: {agent.id}")


if __name__ == "__main__":
    main()
    

from src.services.agent_service import AgentService


def main():

    service = AgentService()

    agent = service.get_agent()

    print(type(agent))

    print("\nAgent Object:\n")
    print(agent)

    print("\nAttributes:\n")
    print(dir(agent))


if __name__ == "__main__":
    main()
    '''

from src.services.agent_service import AgentService

service = AgentService()

agent = service.get_agent()

print(f"Agent Endpoint: {agent.agent_endpoint}")
print(f"Agent Card: {agent.agent_card}")
from src.agent_client import get_project_client
from src.config import AGENT_NAME
from src.config import MODEL_DEPLOYMENT_NAME


class AgentService:

    def __init__(self):
        self.project_client = get_project_client()
        self.openai_client = self.project_client.get_openai_client()

    def get_agent(self):
        agents = self.project_client.agents.list()

        for agent in agents:
            if agent.name == AGENT_NAME:
                return agent

        raise ValueError(f"Agent '{AGENT_NAME}' not found")

    def ask_agent(self, question: str) -> str:

        agent = self.get_agent()

        latest = agent["versions"]["latest"]

        instructions = latest["definition"]["instructions"]

        tools = latest["definition"]["tools"]

        response = self.openai_client.responses.create(
            model=MODEL_DEPLOYMENT_NAME,
            instructions=instructions,
            tools=tools,
            input=question
        )

        return response.output_text
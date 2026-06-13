from src.agent_client import get_project_client
from src.config import AGENT_NAME
from src.config import MODEL_DEPLOYMENT_NAME
from src.logger import logger
import time


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
        
        logger.info(f"User Question: {question}")

        start_time = time.time()

        agent = self.get_agent()

        latest = agent["versions"]["latest"]

        instructions = latest["definition"]["instructions"]

        tools = latest["definition"]["tools"]

        try:

            response = self.openai_client.responses.create(
                model=MODEL_DEPLOYMENT_NAME,
                instructions=instructions,
                tools=tools,
                input=question
            )

            response_time = round(time.time() - start_time, 2)

            logger.info(f"Response Time: {response_time} seconds")

            logger.info("Request Status: Success")

            return response.output_text

        except Exception as e:

            logger.exception("Request Failed")

            raise
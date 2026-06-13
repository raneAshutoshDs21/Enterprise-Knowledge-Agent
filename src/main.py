from src.services.agent_service import AgentService
from src.config import MODEL_DEPLOYMENT_NAME
from src.config import AGENT_NAME


def main():

    print(f"AGENT_NAME = [{AGENT_NAME}]")
    print(f"MODEL_DEPLOYMENT_NAME = [{MODEL_DEPLOYMENT_NAME}]")

    service = AgentService()

    print("=" * 60)
    print("Enterprise Knowledge Assistant")
    print("Type 'exit' to quit")
    print("=" * 60)

    while True:

        question = input("\nYou: ")

        if question.lower() == "exit":
            break

        try:
            answer = service.ask_agent(question)

            print(f"\nAssistant:\n{answer}")

        except Exception as e:
            import traceback
            traceback.print_exc()


if __name__ == "__main__":
    main()
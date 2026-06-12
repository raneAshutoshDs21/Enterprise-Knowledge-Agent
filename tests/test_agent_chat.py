from src.services.agent_service import AgentService


def main():

    service = AgentService()

    question = (
        "How many annual leave days are employees entitled to?"
    )

    print(f"\nQuestion:\n{question}")

    answer = service.ask_agent(question)

    print("\nResponse:\n")
    print(answer)


if __name__ == "__main__":
    main()
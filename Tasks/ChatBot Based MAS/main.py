from agents.executor import ResearcherAgent
from agents.writer import WriterAgent
from agents.validator import ReviewerAgent


def chat_mas():
    researcher = ResearcherAgent()
    writer = WriterAgent()
    reviewer = ReviewerAgent()

    conversation = []

    print("=== Chat-based MAS ===")
    print("Type 'exit' to quit")

    while True:
        user_input = input("\nUser: ")

        if user_input.lower() == "exit":
            break

        # Store user message
        conversation.append(user_input)

        # ---- Researcher ----
        research = researcher.research(conversation)
        print("\n[Researcher]:", research)

        # ---- Writer ----
        draft = writer.write(conversation, research)
        print("\n[Writer]:", draft)

        # ---- Reviewer ----
        final = reviewer.review(conversation, draft)
        print("\n[Reviewer]:", final)

        # Store final response
        conversation.append(final)


if __name__ == "__main__":
    chat_mas()
    
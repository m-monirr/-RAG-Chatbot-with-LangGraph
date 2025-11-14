"""
Main entry point for the RAG chatbot application.
"""

from langchain_core.messages import HumanMessage, AIMessage
from .agent import graph


def print_header():
    """Print the application header."""
    print("=" * 60)
    print("🤖 RAG CHATBOT WITH LANGGRAPH")
    print("=" * 60)
    print("Ask questions about Large Language Models.")
    print("Type 'exit' to quit.\n")


def run_chat_loop():
    """Main chat loop."""
    chat_history = []
    
    while True:
        user_question = input("You: ").strip()
        
        if user_question.lower() == 'exit':
            print("\nGoodbye! 👋")
            break
        
        if not user_question:
            print("Please enter a question.\n")
            continue
        
        print("\n" + "=" * 60)
        print("Processing your question...")
        print("=" * 60)
        
        # Prepare initial state
        initial_state = {
            "question": user_question,
            "documents": [],
            "response": ""
        }
        
        # Execute the graph
        final_state = None
        for output in graph.stream(initial_state):
            node_name = list(output.keys())[0]
            final_state = output[node_name]
        
        # Display answer
        answer = final_state.get("response", "Sorry, I couldn't generate an answer.")
        print("\n" + "=" * 60)
        print(f"\nAI: {answer}\n")
        print("=" * 60 + "\n")


def main():
    """Main entry point."""
    print_header()
    run_chat_loop()


if __name__ == "__main__":
    main()

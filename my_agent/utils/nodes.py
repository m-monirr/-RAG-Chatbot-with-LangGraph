"""
Node functions for the RAG agent graph.
"""

from .state import AgentState
from .tools import get_retriever, get_llm


# Initialize tools
retriever = get_retriever()
llm = get_llm()


def retrieve_documents(state: AgentState) -> AgentState:
    """
    Retrieve relevant documents based on the question.
    
    Args:
        state: Current agent state with question
        
    Returns:
        Updated state with retrieved documents
    """
    print(f"🔍 Retrieving documents for: {state['question']}")
    docs = retriever.invoke(state["question"])
    documents = [doc.page_content for doc in docs]
    print(f"✓ Retrieved {len(documents)} documents\n")
    
    return {
        **state,
        "documents": documents
    }


def generate_response(state: AgentState) -> AgentState:
    """
    Generate a response using the LLM based on retrieved documents.
    
    Args:
        state: Current agent state with question and documents
        
    Returns:
        Updated state with generated response
    """
    print("💭 Generating response...")
    
    context = "\n\n".join(state["documents"])
    prompt = f"""Based on the following context, answer the question.
    
Context:
{context}

Question: {state['question']}

Answer:"""
    
    response = llm.invoke(prompt)
    print("✓ Response generated\n")
    
    return {
        **state,
        "response": response.content
    }

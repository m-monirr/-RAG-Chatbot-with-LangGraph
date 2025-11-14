"""
Main agent graph construction using LangGraph.
"""

from langgraph.graph import StateGraph, END
from .utils.state import AgentState
from .utils.nodes import retrieve_documents, generate_response


def create_graph():
    """
    Create and compile the RAG agent graph.
    
    Returns:
        Compiled graph ready for execution
    """
    # Create the graph
    workflow = StateGraph(AgentState)
    
    # Add nodes
    workflow.add_node("retrieve", retrieve_documents)
    workflow.add_node("generate", generate_response)
    
    # Add edges
    workflow.set_entry_point("retrieve")
    workflow.add_edge("retrieve", "generate")
    workflow.add_edge("generate", END)
    
    # Compile the graph
    graph = workflow.compile()
    
    return graph


# Create the graph instance
graph = create_graph()

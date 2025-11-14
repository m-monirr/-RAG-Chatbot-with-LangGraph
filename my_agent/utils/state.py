"""
State definition for the RAG agent graph.
"""

from typing import TypedDict, List


class AgentState(TypedDict):
    """
    State for the RAG agent workflow.
    
    Attributes:
        question: The user's input question
        documents: Retrieved documents from vector store
        response: Generated response from LLM
    """
    question: str
    documents: List[str]
    response: str

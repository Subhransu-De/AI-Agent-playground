from langchain_ollama import ChatOllama

from typing import Annotated

from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages


class State(TypedDict):
    messages: Annotated[list, add_messages]


def agent(state: State):
    return {"messages": [ChatOllama(model="llama3.1").invoke(state["messages"])]}


def simple_agent():
    chat_graph = (
        StateGraph(State)
        .add_node("agent", agent)
        .add_edge(START, "agent")
        .add_edge("agent", END)
        .compile()
    )

    [
        print(value["messages"][-1].content)
        for event in chat_graph.stream(
            {
                "messages": [
                    (
                        "user",
                        "Can you provide an update on the current state of human civilization?",
                    )
                ]
            }
        )
        for value in event.values()
    ]

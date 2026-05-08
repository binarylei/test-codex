"""A tiny LangGraph Hello World workflow.

This example intentionally avoids any LLM/API-key dependency. It builds a graph
with one node that reads a name from state and writes a greeting back to state.
"""

from typing import TypedDict

from langgraph.graph import END, START, StateGraph


class HelloState(TypedDict):
    """State passed between LangGraph nodes."""

    name: str
    greeting: str


def say_hello(state: HelloState) -> dict[str, str]:
    """Return a greeting update for the current state."""

    return {"greeting": f"Hello, {state['name']}!"}


def build_graph():
    """Build and compile the Hello World LangGraph workflow."""

    graph_builder = StateGraph(HelloState)
    graph_builder.add_node("say_hello", say_hello)
    graph_builder.add_edge(START, "say_hello")
    graph_builder.add_edge("say_hello", END)
    return graph_builder.compile()


def main() -> None:
    """Run the graph from the command line."""

    graph = build_graph()
    result = graph.invoke({"name": "LangGraph", "greeting": ""})
    print(result["greeting"])


if __name__ == "__main__":
    main()

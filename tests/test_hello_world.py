from hello_langgraph.hello_world import build_graph


def test_hello_world_graph_returns_greeting():
    graph = build_graph()

    result = graph.invoke({"name": "LangGraph", "greeting": ""})

    assert result["greeting"] == "Hello, LangGraph!"

# LangGraph Hello World

这是一个最小可运行的 LangGraph Hello World 示例：不需要 LLM 或 API Key，只用一个节点读取 `name`，并把问候语写回 graph state。

## 安装

```bash
python -m pip install -e .
```

## 运行

```bash
hello-langgraph
```

你会看到：

```text
Hello, LangGraph!
```

也可以直接运行模块：

```bash
python -m hello_langgraph.hello_world
```

## 核心代码

```python
from typing import TypedDict
from langgraph.graph import END, START, StateGraph

class HelloState(TypedDict):
    name: str
    greeting: str

def say_hello(state: HelloState) -> dict[str, str]:
    return {"greeting": f"Hello, {state['name']}!"}

graph_builder = StateGraph(HelloState)
graph_builder.add_node("say_hello", say_hello)
graph_builder.add_edge(START, "say_hello")
graph_builder.add_edge("say_hello", END)
graph = graph_builder.compile()

result = graph.invoke({"name": "LangGraph", "greeting": ""})
print(result["greeting"])
```

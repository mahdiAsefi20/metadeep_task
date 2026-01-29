from langgraph.graph import StateGraph, END
from orchestration.graph_state import GraphState
from orchestration.graph_nodes import (
    planner_node,
    storyboard_node,
    verifier_node,
    approve_node,
    fail_node,
)
from orchestration.graph_conditions import (
    route_after_verification,
    route_after_commit,
)


def build_graph():
    graph = StateGraph(GraphState)

    # -----------------
    # Nodes
    # -----------------
    graph.add_node("planner", planner_node)
    graph.add_node("storyboard", storyboard_node)
    graph.add_node("verifier", verifier_node)
    graph.add_node("approve", approve_node)
    graph.add_node("fail", fail_node)

    # -----------------
    # Entry point
    # -----------------
    graph.set_entry_point("planner")

    # -----------------
    # Main forward flow
    # -----------------
    graph.add_edge("planner", "storyboard")
    graph.add_edge("storyboard", "verifier")

    # -----------------
    # Scene-level decision
    # -----------------
    graph.add_conditional_edges(
        "verifier",
        route_after_verification,
        {
            "approve": "approve",
            "fail": "fail",
            "repair": "planner",
        },
    )

    # -----------------
    # Batch-level continuation
    # -----------------
    graph.add_conditional_edges(
        "approve",
        route_after_commit,
        {
            "continue": "storyboard",
            "done": END,
        },
    )

    graph.add_conditional_edges(
        "fail",
        route_after_commit,
        {
            "continue": "storyboard",
            "done": END,
        },
    )

    # -----------------
    # Compile graph
    # -----------------
    return graph.compile()

import json
from orchestration.langgraph_orchestrator import build_graph


def main():

    graph = build_graph()

    initial_state = {
        "scene_plans": [],
        "scenes": [],
        "verification_log": [],
        "retry_budget": {},
    }

    result = graph.invoke(initial_state)

    print(result["scenes"])



if __name__ == "__main__":
    main()



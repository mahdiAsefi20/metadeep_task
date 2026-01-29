import json
from orchestration.langgraph_orchestrator import build_graph
import pprint

def main():

    graph = build_graph()

    initial_state = {
        "scene_plans": [],
        "scenes": [],
        "verification_log": [],
        "retry_budget": {},
    }

    result = graph.invoke(initial_state)

    pprint.pprint(result)



if __name__ == "__main__":
    main()



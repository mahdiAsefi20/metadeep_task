from orchestration.agents import PlannerAgent, StoryboardAgent
from orchestration.verifier import VerifierAgent
from orchestration.state import Scene
from orchestration.graph_state import GraphState

planner = PlannerAgent()
storyboard = StoryboardAgent()
verifier = VerifierAgent()


def planner_node(state: GraphState):   
    if not state.scene_plans and not state.scenes:
        state.scene_plans = planner.create_initial_plan("story")


    # Repair path
    if state.feedback:
        planner.repair_plan(state)

    return state




def storyboard_node(state):
    if not state.scene_plans:
        return state

    plan = state.scene_plans[0]

    dict_scene = storyboard.materialize(plan)

    scene = Scene(**dict_scene)

    state.current_scene = scene
    state.current_plan_id = plan.scene_id
    state.feedback = None
    return state



def verifier_node(state):
    scene = state.current_scene
    if scene is None:
        return state  # nothing to verify

    previous = state.scenes[-1] if state.scenes else None
    feedback = verifier.verify(previous, scene)

    state.feedback = feedback
    return state


def approve_node(state):
    state.scene_plans.pop(0)
    scene = state.current_scene
    scene.status = "approved"
    state.scenes.append(scene)
    return state


def fail_node(state):
    state.scene_plans.pop(0)
    scene = state.current_scene
    scene.status = "failed"
    state.scenes.append(scene)
    return state


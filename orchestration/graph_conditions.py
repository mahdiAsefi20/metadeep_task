def route_after_verification(state):
    feedback = state.feedback
    scene_id = state.current_scene.scene_id

    state.retry_budget.setdefault(scene_id, 0)

    if feedback is None:
        return "approve"

    if state.retry_budget[scene_id] >= 2:
        return "fail"

    state.retry_budget[scene_id] += 1
    return "repair"


def route_after_commit(state):
    if state.scene_plans:
        return "continue"
    return "done"


def insert_retry_budget_and_shift(retry_budget, scene_id):
    new_retry_budget = {}

    for key in sorted(retry_budget):

        if key < scene_id:
            new_retry_budget[key] = retry_budget[key]
        else:
            new_retry_budget[key + 1] = retry_budget[key]

    new_retry_budget[scene_id] = 0
    return new_retry_budget

def insert_scene_and_shift_ids(scene_plans, index, new_scene):

    # Shift scene_ids for scenes at or after the insertion index
    for i in range(index, len(scene_plans)):
        scene_plans[i].scene_id += 1

    # Insert the new scene
    scene_plans.insert(index, new_scene)

    return scene_plans



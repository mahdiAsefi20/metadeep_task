from orchestration.state import ScenePlan
from orchestration.graph_state import GraphState
from orchestration.utils import insert_scene_and_shift_ids, insert_retry_budget_and_shift


class PlannerAgent:

    def create_initial_plan(self, story: str):
        return [
            ScenePlan(scene_id=1, intent="hero in city at night"),
            ScenePlan(scene_id=2, intent="hero appears in desert at noon")
        ]

    def repair_plan(self, state: GraphState):
        feedback = state.feedback
        scene_id = feedback["scene_id"]
        rejection_type = feedback["type"]

        if rejection_type in {"LOCATION_JUMP", "TIME_JUMP"}:
            transition_id = max(p.scene_id for p in state.scenes) + 1

            transition = ScenePlan(
                scene_id=transition_id,
                intent="hero travels between locations"
            )

            index = next(
                (i for i, p in enumerate(state.scene_plans)
                if p.scene_id == scene_id),
                -1
            )

            state.scene_plans = insert_scene_and_shift_ids(state.scene_plans, index, transition)
            state.retry_budget = insert_retry_budget_and_shift(state.retry_budget, transition_id)
            state.verification_log.append(
                f"Inserted transition scene {transition_id} before scene {scene_id + 1}"
            )
            


class StoryboardAgent:

    def materialize(self, plan: ScenePlan):
        if "city" in plan.intent:
            return dict(
                scene_id=plan.scene_id,
                location="city",
                time="night",
                action="hero walks through empty streets"
            )

        if "desert" in plan.intent:
            return dict(
                scene_id=plan.scene_id,
                location="desert",
                time="noon",
                action="hero stands under the sun"
            )

        if "travels" in plan.intent:
            return dict(
                scene_id=plan.scene_id,
                location="road",
                time="morning",
                action="hero travels between locations"
            )

        return dict(
            scene_id=plan.scene_id,
            location="unknown",
            time="unknown",
            action="hero exists"
        )

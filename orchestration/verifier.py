from orchestration.state import Scene


class VerifierAgent:

    def verify(self, previous: Scene | None, current: Scene):
        if previous:
            if previous.location != current.location:
                if current.location != "road" and previous.location != "road":
                    return {
                        "scene_id": current.scene_id,
                        "type": "LOCATION_JUMP",
                        "message": "Location changed without transition"
                    }

            if previous.time == "night" and current.time == "noon":
                return {
                    "scene_id": current.scene_id,
                    "type": "TIME_JUMP",
                    "message": "Invalid time jump detected"
                }

        if " and " in current.action:
            return {
                "scene_id": current.scene_id,
                "type": "MULTIPLE_ACTIONS",
                "message": "Multiple actions in a single scene"
            }

        return None

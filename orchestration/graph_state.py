from typing import List, Dict, Optional
from orchestration.state import ScenePlan, Scene
from dataclasses import dataclass, field


@dataclass
class GraphState:
    scene_plans: List[ScenePlan] = field(default_factory=list)
    scenes: List[Scene] = field(default_factory=list)
    verification_log: List[str] = None
    current_scene: Optional[Scene] = None
    current_plan_id: Optional[int] = None
    feedback: Optional[dict] = None
    retry_budget: Dict[int, int] = field(default_factory=dict)
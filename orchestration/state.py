from dataclasses import dataclass, field
from typing import List, Dict, Optional


@dataclass
class ScenePlan:
    scene_id: int
    intent: str


@dataclass
class Scene:
    scene_id: int
    location: str
    time: str
    action: str
    status: str = "pending"
    revision_reason: Optional[str] = None


@dataclass
class OrchestrationState:
    scene_plans: List[ScenePlan] = field(default_factory=list)
    scenes: List[Scene] = field(default_factory=list)
    verification_log: List[str] = field(default_factory=list)
    retry_budget: Dict[int, int] = field(default_factory=dict)
    max_retries: int = 2

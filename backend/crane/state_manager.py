from .crane import Crane
from .models import CraneState, Origin
from typing import Dict, Tuple


class StateManager:
    def __init__(self, crane: Crane):
        self.crane = crane

    def update_state(self, new_state: Dict[str, float]):
        current_state = self.crane.state
        updated_state = CraneState(
            swing=new_state.get('swing', current_state.swing),
            lift=new_state.get('lift', current_state.lift),
            elbow=new_state.get('elbow', current_state.elbow),
            wrist=new_state.get('wrist', current_state.wrist),
            gripper=new_state.get('gripper', current_state.gripper)
        )
        self.crane.update_state(updated_state)

    def solve_ik(self, target_position: Tuple[float, float, float]):
        self.crane.perform_ik(*target_position)

    def update_origin(self, new_origin: Origin):
        self.crane.set_origin(new_origin)

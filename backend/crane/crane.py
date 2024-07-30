from .models import CraneState, Origin
import numpy as np


class Crane:
    def __init__(self):
        self.state = CraneState(swing=0, lift=0, elbow=0, wrist=0, gripper=0)
        self.origin = Origin(x=0, y=0, z=0, rotation=0)
        self.max_speeds = {
            'swing': 1.0,
            'lift': 1.0,
            'elbow': 1.0,
            'wrist': 1.0,
            'gripper': 1.0
        }
        self.time_step = 0.1

    def update_state(self, new_state: CraneState):
        for actuator in self.state.__annotations__.keys():
            current_value = getattr(self.state, actuator)
            target_value = getattr(new_state, actuator)
            max_delta = self.max_speeds[actuator] * self.time_step
            if abs(target_value - current_value) > max_delta:
                if target_value > current_value:
                    setattr(self.state, actuator, current_value + max_delta)
                else:
                    setattr(self.state, actuator, current_value - max_delta)
            else:
                setattr(self.state, actuator, target_value)

    def perform_ik(self, x: float, y: float, z: float):
        self.state.lift = z
        self.state.swing = np.degrees(np.arctan2(y, x))

    def set_origin(self, new_origin: Origin):
        self.origin = new_origin

    def to_dict(self):
        return {
            'state': self.state.model_dump(),
            'origin': self.origin.model_dump()
        }

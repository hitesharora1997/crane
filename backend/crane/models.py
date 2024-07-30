from pydantic import BaseModel


class CraneState(BaseModel):
    swing: float
    lift: float
    elbow: float
    wrist: float
    gripper: float


class Origin(BaseModel):
    x: float
    y: float
    z: float
    rotation: float

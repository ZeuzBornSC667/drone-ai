from dataclasses import dataclass


@dataclass
class PositionSetpoint:
    x: float
    y: float
    z: float

import time
from dataclasses import dataclass

@dataclass
class Vec3:
    x: float = 0
    y: float = 0
    z: float = 0

@dataclass
class Attitude:
    roll: float = 0
    pitch: float = 0
    yaw: float = 0

@dataclass
class Motors:
    front_left: float = 0
    front_right: float = 0
    rear_left: float = 0
    rear_right: float = 0

class DroneState:
    def __init__(self):
        self.position = Vec3()
        self.velocity = Vec3()
        self.attitude = Attitude()
        self.motors = Motors()

        self.battery_percentage = 100.0
        self.altitude_barometric = 0.0
        self.signal_strength = 100.0

        self.is_armed = False
        self.is_flying = False
        self.flight_mode = "IDLE"

        self.nn_confidence = 0.0

        self.frame_id = 0
        self.timestamp = time.time()

    def to_dict(self):
        self.frame_id += 1
        self.timestamp = time.time()
        return self.__dict__

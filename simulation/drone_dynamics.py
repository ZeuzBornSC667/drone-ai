"""
simulation/drone_dynamics.py

Simplified quadrotor dynamics for PPO training.

State:
- position (x,y,z)
- velocity (vx,vy,vz)
- attitude (roll,pitch,yaw)

Action:
[throttle, roll_cmd, pitch_cmd, yaw_cmd]
range: [-1, 1]

Designed for deterministic fixed-timestep simulation.
"""

from dataclasses import dataclass
import numpy as np


@dataclass
class DroneState:

    position: np.ndarray
    velocity: np.ndarray

    roll: float
    pitch: float
    yaw: float

    battery: float

    motors: np.ndarray


class DroneDynamics:

    DT = 0.02

    MASS = 1.0

    GRAVITY = 9.81

    MAX_THRUST = 20.0

    def __init__(self):

        self.target = np.array(
            [0.0, 0.0, 5.0],
            dtype=np.float32
        )

        self.reset()

    def reset(self):

        self.state = DroneState(
            position=np.zeros(3, dtype=np.float32),
            velocity=np.zeros(3, dtype=np.float32),

            roll=0.0,
            pitch=0.0,
            yaw=0.0,

            battery=100.0,

            motors=np.zeros(4, dtype=np.float32)
        )

        return self.state

    def apply_action(self, action):

        action = np.asarray(action, dtype=np.float32)

        action = np.clip(action, -1.0, 1.0)

        self.state.motors = (action + 1.0) / 2.0

    def step(self):

        thrust = np.mean(self.state.motors)

        thrust_force = thrust * self.MAX_THRUST

        az = thrust_force / self.MASS - self.GRAVITY

        self.state.velocity[2] += az * self.DT

        self.state.position += self.state.velocity * self.DT

        self.state.battery = max(
            0.0,
            self.state.battery - 0.001
        )

        return self.state
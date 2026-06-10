import gymnasium as gym
import numpy as np

from gymnasium import spaces

from simulation.drone_dynamics import DroneDynamics
from rl.envs.reward_function import compute_reward


class DroneEnv(gym.Env):

    metadata = {"render_modes": []}

    def __init__(self):
        super().__init__()

        self.sim = DroneDynamics()

        self.max_steps = 1000
        self.step_count = 0

        self.action_space = spaces.Box(
            low=-1.0,
            high=1.0,
            shape=(4,),
            dtype=np.float32
        )

        self.observation_space = spaces.Box(
            low=-np.inf,
            high=np.inf,
            shape=(18,),
            dtype=np.float32
        )

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)

        self.step_count = 0

        self.sim.reset()

        obs = self._get_obs()

        return obs, {}

    def step(self, action):

        self.step_count += 1

        self.sim.apply_action(action)
        self.sim.step()

        state = self.sim.state

        obs = self._get_obs()

        reward = compute_reward(
            state=state,
            action=action,
            target=self.sim.target
        )

        altitude_error = abs(
            self.sim.target[2]
            - state.position[2]
        )

        success = altitude_error < 0.10

        crashed = self._is_crashed()

        if crashed:
            reward -= 100.0

        if success:
            reward += 100.0

        terminated = (
            crashed or success
        )

        truncated = (
            self.step_count >= self.max_steps
        )

        return (
            obs,
            reward,
            terminated,
            truncated,
            {}
        )

    def _get_obs(self):

        state = self.sim.state
        target = self.sim.target

        distance = np.linalg.norm(
            target - state.position
        )

        obs = np.array([

            state.position[0] / 10.0,
            state.position[1] / 10.0,
            state.position[2] / 10.0,

            state.velocity[0] / 5.0,
            state.velocity[1] / 5.0,
            state.velocity[2] / 5.0,

            state.roll / 45.0,
            state.pitch / 45.0,
            state.yaw / 180.0,

            target[0] / 10.0,
            target[1] / 10.0,
            target[2] / 10.0,

            distance / 20.0,

            state.battery / 100.0,

            state.motors[0],
            state.motors[1],
            state.motors[2],
            state.motors[3]

        ], dtype=np.float32)

        return obs

    def _is_crashed(self):

        s = self.sim.state

        return (
            s.position[2] < 0
            or abs(s.roll) > 80
            or abs(s.pitch) > 80
        )
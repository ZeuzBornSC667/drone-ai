
import gymnasium as gym
import numpy as np

class DroneTrajectoryEnv(gym.Env):
    def __init__(self):
        self.observation_space = gym.spaces.Box(-10,10,(12,))
        self.action_space = gym.spaces.Box(-1,1,(5,))

        self.state = np.zeros(12)
        self.target = np.array([5,5,3])

    def reset(self, seed=None, options=None):
        return self.state, {}

    def step(self, action):
        self.state[:3] += action[:3] * 0.1
        dist = np.linalg.norm(self.target - self.state[:3])
        reward = -dist
        return self.state, reward, dist < 0.2, False, {}


import gymnasium as gym
import numpy as np

class DroneEnv(gym.Env):
    def __init__(self):
        self.action_space = gym.spaces.Box(low=-1, high=1, shape=(4,))
        self.observation_space = gym.spaces.Box(low=-1, high=1, shape=(10,))

    def reset(self, seed=None, options=None):
        return np.zeros(10), {}

    def step(self, action):
        obs = np.random.randn(10)

        # PPO SAFE reward: trajectory-level only
        reward = -float((action**2).sum())

        done = False
        return obs, reward, done, False, {}

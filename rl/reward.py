
import numpy as np

def reward_fn(state, target):
    return -np.linalg.norm(np.array(state[:3]) - np.array(target))

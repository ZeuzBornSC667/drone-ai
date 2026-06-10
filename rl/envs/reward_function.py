"""
Reward shaping for PPO hover training.

Goal:
    Reach target altitude
    Stay stable
    Minimize control effort
"""

import numpy as np


def compute_reward(state, action, target):

    pos = state.position

    target_z = target[2]

    altitude_error = abs(
        target_z - pos[2]
    )

    # Core shaping signal
    r_altitude = -altitude_error

    # Reward getting close to target altitude
    if altitude_error < 0.50:
        r_altitude += 2.0

    if altitude_error < 0.25:
        r_altitude += 5.0

    if altitude_error < 0.10:
        r_altitude += 10.0

    # Stability reward
    r_stability = -(
        abs(state.roll)
        + abs(state.pitch)
    ) * 0.05

    # Smooth control
    r_energy = (
        -np.sum(np.square(action))
        * 0.005
    )

    # Survive bonus
    r_alive = 0.1

    reward = (
        r_altitude
        + r_stability
        + r_energy
        + r_alive
    )

    return float(reward)
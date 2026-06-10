import numpy as np

from simulation.drone_dynamics import DroneState
from rl.envs.reward_function import compute_reward


target = np.array(
    [0.0, 0.0, 5.0],
    dtype=np.float32
)

action = np.zeros(
    4,
    dtype=np.float32
)


def evaluate(z):

    state = DroneState(
        position=np.array(
            [0.0, 0.0, z],
            dtype=np.float32
        ),

        velocity=np.zeros(
            3,
            dtype=np.float32
        ),

        roll=0.0,
        pitch=0.0,
        yaw=0.0,

        battery=100.0,

        motors=np.zeros(
            4,
            dtype=np.float32
        )
    )

    reward = compute_reward(
        state,
        action,
        target
    )

    print(
        f"Altitude {z:>5.2f} m -> Reward {reward:>8.3f}"
    )


evaluate(0.0)
evaluate(2.0)
evaluate(4.0)
evaluate(5.0)
evaluate(6.0)
evaluate(10.0)
"""
rl/train/train_ppo.py
Production PPO training.
"""

"""
rl/train/train_ppo.py

Production PPO trainer for DroneEnv.
"""

from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv
from stable_baselines3.common.vec_env import VecNormalize
from stable_baselines3.common.callbacks import CheckpointCallback
from stable_baselines3.common.monitor import Monitor

from rl.envs.drone_env import DroneEnv


def make_env():
    return Monitor(
        DroneEnv()
    )


if __name__ == "__main__":

    env = DummyVecEnv(
        [make_env for _ in range(8)]
    )

    env = VecNormalize(
        env,
        norm_obs=True,
        norm_reward=True,
        clip_obs=10.0
    )

    checkpoint_callback = CheckpointCallback(
        save_freq=10000,
        save_path="models/checkpoints",
        name_prefix="ppo_hover"
    )

    model = PPO(
        "MlpPolicy",
        env,

        verbose=1,

        learning_rate=3e-4,

        n_steps=2048,

        batch_size=256,

        gamma=0.99,

        gae_lambda=0.95,

        clip_range=0.2,

        ent_coef=0.01,

        tensorboard_log="./runs/ppo_hover"
    )

    model.learn(
        total_timesteps=100_000,
        callback=checkpoint_callback
    )

    model.save(
        "models/hover_policy"
    )

    env.save(
        "models/vec_normalize.pkl"
    )

    print("Training complete")
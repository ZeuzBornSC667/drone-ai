
from stable_baselines3 import PPO

def create_model(env):
    return PPO("MlpPolicy", env, verbose=1,
               learning_rate=3e-4,
               n_steps=2048,
               batch_size=64,
               gamma=0.99,
               clip_range=0.2,
               ent_coef=0.01)

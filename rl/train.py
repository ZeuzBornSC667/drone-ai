
from envs.drone_env import DroneTrajectoryEnv
from rl.ppo_agent import create_model

env = DroneTrajectoryEnv()
model = create_model(env)
model.learn(1_000_000)
model.save("ppo_drone")

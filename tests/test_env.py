from rl.envs.drone_env import DroneEnv

env = DroneEnv()

obs, info = env.reset()

for _ in range(100):

    action = env.action_space.sample()

    obs, reward, terminated, truncated, info = env.step(action)

    if terminated or truncated:
        obs, info = env.reset()

print("Environment OK")

class TrajectoryPlanner:
    def __init__(self):
        self.target = None

    def step(self, state, action):
        dx, dy, dz, dyaw, t = action

        self.target = {
            "x": state.position.x + dx,
            "y": state.position.y + dy,
            "z": max(0, state.position.z + dz),
            "yaw": state.attitude.yaw + dyaw,
            "t": t
        }
        return self.target

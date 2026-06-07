
class PIDAttitude:
    def compute(self, vel, state):
        return vel[1], vel[0], state.attitude.yaw

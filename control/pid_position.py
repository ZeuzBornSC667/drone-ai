
class PIDPosition:
    def __init__(self, kp=1.2):
        self.kp = kp

    def compute(self, target, state):
        return (
            self.kp * (target["x"] - state.position.x),
            self.kp * (target["y"] - state.position.y),
            self.kp * (target["z"] - state.position.z),
        )

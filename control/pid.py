
class PID:
    def __init__(self, kp, ki, kd):
        self.kp, self.ki, self.kd = kp, ki, kd
        self.i = 0
        self.prev = 0

    def update(self, error, dt):
        self.i += error * dt
        d = (error - self.prev) / dt if dt else 0
        self.prev = error
        return self.kp*error + self.ki*self.i + self.kd*d

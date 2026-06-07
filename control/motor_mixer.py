
class MotorMixer:
    def mix(self, roll, pitch, yaw):
        return {
            "front_left": pitch - roll + yaw,
            "front_right": pitch + roll - yaw,
            "rear_left": -pitch - roll - yaw,
            "rear_right": -pitch + roll - yaw,
        }

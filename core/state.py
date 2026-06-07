
class DroneState:
    def __init__(self):
        self.drone_id = "DRONE_001"
        self.frame_id = 0
        self.timestamp = 0.0
        self.position = type('p',(object,),{'x':0,'y':0,'z':0})()
        self.attitude = type('a',(object,),{'roll':0,'pitch':0,'yaw':0})()
        self.motors = type('m',(object,),{'front_left':0,'front_right':0,'rear_left':0,'rear_right':0})()
        self.battery_percentage = 100
        self.altitude_barometric = 0
        self.is_armed = False
        self.is_flying = False
        self.flight_mode = "IDLE"
        self.nn_confidence = 0.0
        self.signal_strength = 100

    def to_dict(self):
        return self.__dict__

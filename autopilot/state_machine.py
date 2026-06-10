from enum import Enum


class FlightState(Enum):

    DISARMED = 0
    ARMED = 1
    TAKEOFF = 2
    MISSION = 3
    RTL = 4
    LAND = 5
    FAILSAFE = 6
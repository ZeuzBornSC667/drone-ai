from enum import Enum


class FlightMode(Enum):

    MANUAL = 0
    ALT_HOLD = 1
    POS_HOLD = 2
    MISSION = 3
    RL_GUIDED = 4
    RTL = 5
    LAND = 6
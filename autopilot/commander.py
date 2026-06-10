"""
PX4-style Commander.

Responsible for:
- Arming/disarming
- Flight mode transitions
- Failsafe activation
"""

from autopilot.state_machine import FlightState


class Commander:

    def __init__(self):
        self.state = FlightState.DISARMED

    def arm(self):
        pass

    def disarm(self):
        pass

    def set_mode(self, mode):
        pass

    def update(self):
        pass
"""Discrete PI controller for the room heater. Built test first, see SPEC-example.md."""


class PIController:
    def __init__(self, dt):
        self.dt = dt  # s

    def update(self, setpoint, measurement):
        """Return the actuator command u in percent."""
        return 0.0

"""Discrete PI controller for the room heater. Built test first, see SPEC-example.md."""


class PIController:
    def __init__(self, dt, kp=100.0, ti=900.0):
        self.dt = dt  # s
        self.kp = kp  # %/K
        self.ti = ti  # s
        self.integral = 0.0  # %

    def update(self, setpoint, measurement):
        """Return the actuator command u in percent."""
        error = setpoint - measurement
        integral = self.integral + self.kp * self.dt / self.ti * error
        u = self.kp * error + integral
        if 0.0 <= u <= 100.0:
            self.integral = integral  # integrate only when not saturated, against windup
        return min(100.0, max(0.0, u))

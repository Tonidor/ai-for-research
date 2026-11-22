"""Discrete PI controller for the room heater."""


class PIController:
    def __init__(self, kp=30.0, ki=0.05, dt=10.0, u_min=0.0, u_max=100.0):
        self.kp = kp        # % per K
        self.ki = ki        # % per K per s
        self.dt = dt        # s
        self.u_min = u_min
        self.u_max = u_max
        self.integral = 0.0

    def update(self, setpoint, measurement):
        """Return the heater power in percent."""
        error = setpoint - measurement
        self.integral += error * self.dt
        u = self.kp * error + self.ki * self.integral
        return min(max(u, self.u_min), self.u_max)

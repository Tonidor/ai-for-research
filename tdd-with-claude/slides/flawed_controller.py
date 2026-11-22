"""Discrete PI controller for room temperature regulation."""

from dataclasses import dataclass, field


@dataclass
class PIController:
    """Discrete-time PI controller with output saturation.

    Computes the heater command u = Kp * e + Ki * integral(e dt),
    clamped to the actuator range [u_min, u_max].

    Attributes:
        dt: Sample time in seconds.
        kp: Proportional gain in % per K.
        ki: Integral gain in % per K per second.
        u_min: Lower actuator limit in %.
        u_max: Upper actuator limit in %.
    """

    dt: float
    kp: float = 30.0
    ki: float = 0.05
    u_min: float = 0.0
    u_max: float = 100.0
    _integral: float = field(default=0.0, init=False, repr=False)

    def update(self, setpoint: float, measurement: float) -> float:
        """Advance the controller by one sample.

        Args:
            setpoint: Desired room temperature in °C.
            measurement: Measured room temperature in °C.

        Returns:
            Heater command in %, within [u_min, u_max].
        """
        error = setpoint - measurement
        self._integral += error * self.dt
        u = self.kp * error + self.ki * self._integral
        return self._clamp(u)

    def reset(self) -> None:
        """Reset the integrator state."""
        self._integral = 0.0

    def _clamp(self, u: float) -> float:
        return min(max(u, self.u_min), self.u_max)

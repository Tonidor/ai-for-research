"""First-order thermal model of a room with an electric heater."""


class Room:
    """C dT/dt = (T_out - T) / R + P_max * u / 100 - Q_window

    u is the heater power in percent. Q_window is extra heat loss in watts.
    """

    def __init__(self, temp=19.0, outdoor=5.0, R=0.01, C=360_000.0, p_max=3000.0):
        self.temp = temp
        self.outdoor = outdoor
        self.R = R          # thermal resistance to outside, K/W
        self.C = C          # heat capacity, J/K (time constant R*C = 1 h)
        self.p_max = p_max  # heater power at 100 %, W

    def step(self, power, dt, window_loss=0.0):
        """Advance the room by dt seconds and return the new temperature."""
        heat_in = self.p_max * power / 100
        heat_out = (self.temp - self.outdoor) / self.R + window_loss
        self.temp += dt * (heat_in - heat_out) / self.C
        return self.temp

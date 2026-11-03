"""Room model and test bench for the heater controller.

Run `python heater.py` to plot both scenarios from SPEC.md.
"""

from controller import PIController

DT = 10.0  # s
WINDOW_OPEN = (3 * 3600, 4 * 3600)  # s
WINDOW_CONDUCTANCE = {"small": 37.5, "large": 125.0}  # W/K, 0.6 and 2 kW at 21 °C


class Room:
    """First-order thermal model: C dT/dt = (1/R + G_window) (T_out - T) + P_max u / 100"""

    def __init__(self, temp=19.0, outdoor=5.0, R=0.01, C=360_000.0, p_max=3000.0):
        self.temp = temp
        self.outdoor = outdoor
        self.R = R          # K/W, wall loss 1.6 kW at 21 °C
        self.C = C          # J/K, time constant R C = 1 h
        self.p_max = p_max  # W

    def step(self, u, window_conductance):
        heat_in = self.p_max * u / 100
        heat_out = (1 / self.R + window_conductance) * (self.temp - self.outdoor)
        self.temp += DT * (heat_in - heat_out) / self.C


def simulate(window, controller=None, setpoint=21.0, hours=7):
    """Run one scenario, "small" or "large". Return time (s), temperature (°C), u (%)."""
    room = Room()
    controller = controller or PIController(dt=DT)
    times, temps, commands = [], [], []
    for k in range(int(hours * 3600 / DT)):
        t = k * DT
        u = controller.update(setpoint, room.temp)
        is_open = WINDOW_OPEN[0] <= t < WINDOW_OPEN[1]
        times.append(t)
        temps.append(room.temp)
        commands.append(u)
        room.step(u, WINDOW_CONDUCTANCE[window] if is_open else 0.0)
    return times, temps, commands


def plot(controller_class=PIController, filename="heater.png"):
    """Plot both scenarios, temperature on top and u below, and save to filename."""
    import matplotlib.pyplot as plt

    fig, axes = plt.subplots(2, 2, sharex=True, sharey="row", figsize=(10, 6))
    for col, window in enumerate(WINDOW_CONDUCTANCE):
        times, temps, commands = simulate(window, controller=controller_class(dt=DT))
        hours = [t / 3600 for t in times]
        axes[0, col].set_title(f"{window} window")
        axes[0, col].plot(hours, temps)
        axes[0, col].axhline(21.0, color="gray", linestyle="--")
        axes[1, col].plot(hours, commands)
        axes[1, col].set_xlabel("Time (h)")
        for ax in axes[:, col]:
            ax.axvspan(*(t / 3600 for t in WINDOW_OPEN), color="gray", alpha=0.15)
        axes[0, col].text(3.5, 0.97, "window\nopen", ha="center", va="top", color="dimgray",
                          transform=axes[0, col].get_xaxis_transform())
    axes[0, 0].set_ylim(0, 30)
    axes[1, 0].set_ylim(-5, 105)
    axes[0, 0].set_ylabel("Temperature (°C)")
    axes[1, 0].set_ylabel("u (%)")
    fig.tight_layout()
    fig.savefig(filename, dpi=150)
    print(f"Saved {filename}")


if __name__ == "__main__":
    plot()

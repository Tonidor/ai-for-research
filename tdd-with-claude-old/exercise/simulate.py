"""Closed-loop simulation of the room and the controller."""

from controller import PIController
from room import Room


def simulate(room=None, controller=None, setpoint=21.0, duration=3 * 3600, dt=10.0,
             window=None):
    """Run the loop for duration seconds.

    window is (start_s, end_s, loss_W): a window that is open from start to end.
    Returns lists of time (s), temperature (degC) and heater power (%).
    """
    room = room or Room()
    controller = controller or PIController(dt=dt)
    times, temps, powers = [], [], []
    for k in range(int(duration / dt)):
        t = k * dt
        power = controller.update(setpoint, room.temp)
        loss = window[2] if window and window[0] <= t < window[1] else 0.0
        times.append(t)
        temps.append(room.temp)
        powers.append(power)
        room.step(power, dt, loss)
    return times, temps, powers

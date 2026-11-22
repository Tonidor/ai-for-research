import pytest

from heater import simulate

R = 21.0  # °C
BAND = 0.2  # K
SCENARIOS = ["small", "large"]


def run(window):
    times, temps, commands = simulate(window)
    return [t / 3600 for t in times], temps, commands


def settles(hours, temps, start, end):
    """True if T is in the band from 30 min after start until end (h)."""
    return all(abs(T - R) <= BAND for h, T in zip(hours, temps) if start + 0.5 <= h < end)


def test_simulation_runs():
    times, temps, commands = simulate("small")
    assert len(times) == len(temps) == len(commands) == 7 * 360


@pytest.mark.parametrize("window", SCENARIOS)
def test_command_within_limits(window):
    _, _, commands = run(window)
    assert all(0 <= u <= 100 for u in commands)


@pytest.mark.parametrize("window", SCENARIOS)
def test_converges_within_30_min(window):
    hours, temps, _ = run(window)
    assert settles(hours, temps, 0, 3)


@pytest.mark.parametrize("window", SCENARIOS)
def test_no_overshoot(window):
    _, temps, _ = run(window)
    assert max(temps) <= R + 0.5


@pytest.mark.parametrize("window", SCENARIOS)
def test_tracks_setpoint(window):
    hours, temps, _ = run(window)
    assert abs(temps[hours.index(3.0)] - R) <= 0.05
    assert abs(temps[-1] - R) <= 0.05


def test_small_window_dip_is_small():
    hours, temps, _ = run("small")
    assert min(T for h, T in zip(hours, temps) if 3 <= h < 4) >= R - 0.5


def test_small_window_recovers():
    hours, temps, _ = run("small")
    assert settles(hours, temps, 3, 4)
    assert settles(hours, temps, 4, 7)


def test_large_window_saturates():
    hours, _, commands = run("large")
    assert all(u == 100 for h, u in zip(hours, commands) if 3.25 <= h < 4)


def test_large_window_recovers():
    hours, temps, _ = run("large")
    assert settles(hours, temps, 4, 7)

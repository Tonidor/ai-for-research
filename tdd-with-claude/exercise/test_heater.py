from heater import simulate


def test_simulation_runs():
    times, temps, commands = simulate("small")
    assert len(times) == len(temps) == len(commands) == 7 * 360

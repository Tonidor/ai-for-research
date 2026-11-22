from simulate import simulate


def test_simulation_runs():
    times, temps, powers = simulate(duration=600, dt=10.0)
    assert len(times) == len(temps) == len(powers) == 60

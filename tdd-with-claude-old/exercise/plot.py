"""Plot the step response to step_response.png: python plot.py"""

import matplotlib.pyplot as plt

from simulate import simulate

times, temps, powers = simulate()
minutes = [t / 60 for t in times]

fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
ax1.plot(minutes, temps)
ax1.axhline(21.0, color="gray", linestyle="--")
ax1.set_ylabel("Temperature (°C)")
ax2.plot(minutes, powers)
ax2.set_ylabel("Heater power (%)")
ax2.set_xlabel("Time (min)")
fig.savefig("step_response.png")

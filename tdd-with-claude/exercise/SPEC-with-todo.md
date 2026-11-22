---
tags:
  - ai-generated
---
# Heater controller spec

Discrete PI controller for a room heater.
- Setpoint $r = 21$ °C. Room time constant 1 h.
- Actuator command $u \in [0, 100]\,\%$: the share of the heater's maximum power.

## Scenarios

Two separate 7 h runs, each starting at 19 °C, with a window open from 3 h to 4 h:
1. **Small window:** holding $r$ needs $u \approx 73\,\%$.
2. **Large window:** holding $r$ would need $u \approx 120\,\%$, so $r$ is unreachable while the window is open.

## Requirements

Band: $|T - r| \le 0.2$ K. All times are from the start of a run.

1. **Limits:** $0 \le u \le 100\,\%$ at every step.
2. **Fast convergence:** from 19 °C, $T$ enters the band within 30 min and stays in it until 3 h.
3. **Small overshoot:** $T \le 21.5$ °C at all times, in both scenarios.
4. **Good tracking:** $|T - r| \le 0.05$ K at 3 h and at 7 h, in both scenarios.
5. **Disturbance rejection, small window:** $T \ge 20.5$ °C while the window is open.
   $T$ is back in the band within 30 min after the window opens and after it closes.
6. **Disturbance rejection, large window:** $u = 100\,\%$ from 3.25 h until the window
   closes. $T$ is back in the band within 30 min after the window closes.

Low energy use is not a separate requirement. The room's losses set the energy. The only
waste a controller can add is heating above $r$, which 3 and 6 rule out.

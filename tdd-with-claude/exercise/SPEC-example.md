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

In both runs, after the start and after the window closes:
1. Steady-state error < 0.05 °C
2. Overshoot < 1 °C
3. Settling time to ± 0.2 °C < 1 h

At all times:

4. $u$ within 0–100 %

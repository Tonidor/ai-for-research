---
tags:
  - ai-generated
---
# Heater controller spec

Discrete PI controller for a room heater.
- Setpoint $r = 21$ °C. Room time constant 1 h.
- Actuator command $u \in [0, 100]\,\%$.

## Scenarios

Two separate 7 h runs, each starting at 19 °C, with a window open from 3 h to 4 h:
1. **Small window:** holding $r$ needs $u \approx 73\,\%$.
2. **Large window:** holding $r$ would need $u \approx 120\,\%$, so $r$ is unreachable while the window is open.

## Requirements

TODO: What would you test?

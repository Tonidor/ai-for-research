---
tags:
  - ai-generated
---
# Room heater controller spec

A PI controller heats a room to a setpoint of 21 °C. The heater power is between 0 and 100 %.
The model is in `room.py`, the controller in `controller.py`, the loop in `simulate.py`.

Unless a requirement says otherwise, the room starts at 19 °C, it is 5 °C outside, and the
simulation step is 10 s.

## Requirements

1. **Reaches the setpoint.** After 3 h the temperature is within 0.05 °C of 21 °C.
2. **Small overshoot.** The temperature never goes above 21.5 °C.
3. **Settles fast.** After 30 min the temperature stays within 21 ± 0.2 °C.
4. **Respects the heater limits.** The heater power is always between 0 and 100 %.
5. **Calm at the setpoint.** Once settled, the heater power stays constant. In the last hour of
   a 3 h run it changes by less than 0.1 %.
6. **Recovers from an open window.** A window opens after 3 h and closes after 4 h. It costs an
   extra 600 W. Within 30 min after it closes, the temperature is back within 21 ± 0.2 °C.
7. **No large overshoot after long saturation.** A big window opens after 3 h and closes after
   4 h. It costs an extra 2000 W, more than the heater can make up, so the heater runs at 100 %
   for about an hour. After the window closes, the temperature never goes above 22 °C.

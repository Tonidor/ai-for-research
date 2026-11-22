"""Plot the flawed controller for the hook slide: python hook_plot.py"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "exercise"))
from heater import plot  # noqa: E402
from flawed_controller import PIController  # noqa: E402

plot(PIController, "hook.png")

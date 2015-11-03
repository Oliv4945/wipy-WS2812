Wipy-MicroPython WS2812 driver
=========================

Wipy-MicroPython driver for WS2812, WS2812B, and compatible RGB LEDs. These are
popular RGB LEDs used for example in AdaFruit NeoPixels rings, strips, boards,
etc.

Driver has been tested with up to 16 LEDs (for now) but it
should work with much more LEDs.

Installation
------------

Copy `ws2812.py` file to your pyboard.

Usage
-----

```
from ws2812 import WS2812
chain = WS2812( ledNumber=4 )
data = [
    (255, 0, 0),    # red
    (0, 255, 0),    # green
    (0, 0, 255),    # blue
    (85, 85, 85),   # white
]
chain.show(data)
```

Wiring
------

WS2812 driver is using SPI bus. Connect your LED's input wire to the SPI bus 0
MOSI (pin GP16 on Wipy) Connect LED's power and ground wires to VIN and GND.
The same applies for LED rings, stripes, etc. (they have always one input wire).

USB may be insufficient for powering lots of RGB LEDs. You may need to use
additional power source.

More info & Help
----------------

You can check more about the MicroPython project here: http://micropython.org

Discussion about this driver: http://forum.micropython.org/viewtopic.php?f=5&t=394

Changelog
---------

* 1.0 - First release.

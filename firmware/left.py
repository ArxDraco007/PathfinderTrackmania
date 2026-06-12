import board
import digitalio
import usb_hid
import keypad
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

kbd = Keyboard(usb_hid.devices)

BUTTON_PINS = (
    board.D0,  # GAS    - GPIO26/A0
    board.D1,  # BRAKE  - GPIO27/A1
    board.D2,  # LEFT   - GPIO28/A2
    board.D3,  # RIGHT  - GPIO29/A3
    board.D4,  # AK60   - GPIO6/SDA
    board.D5,  # POWER  - GPIO7/SCL
)

KEYCODES = (
    Keycode.UP_ARROW,    # GAS
    Keycode.DOWN_ARROW,  # BRAKE
    Keycode.LEFT_ARROW,  # LEFT
    Keycode.RIGHT_ARROW, # RIGHT
    Keycode.THREE,       # AK60
    Keycode.ONE,         # POWER (set to your needed key)
)

keys = keypad.Keys(BUTTON_PINS, value_when_pressed=False, pull=True)

# POWER LED - always on, using a spare pin (e.g. D6 = GPIO3/MOSI on U2)
power_led = digitalio.DigitalInOut(board.D6)
power_led.direction = digitalio.Direction.OUTPUT
power_led.value = True

while True:
    event = keys.events.get()

    if event:
        key_idx = event.key_number

        if event.pressed:
            kbd.press(KEYCODES[key_idx])

        if event.released:
            kbd.release(KEYCODES[key_idx])
import board
import digitalio
import usb_hid
import keypad
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

kbd = Keyboard(usb_hid.devices)

# U2 - GPIO26,27,28,29,6,7 = D0-D5 on XIAO
BUTTON_PINS = (
    board.D0,  # GAS    (GPIO26/A0)
    board.D1,  # BRAKE  (GPIO27/A1)
    board.D2,  # LEFT   (GPIO28/A2)
    board.D3,  # RIGHT  (GPIO29/A3)
    board.D4,  # AK60   (GPIO6/SDA)
    board.D5,  # POWER  (GPIO7/SCL)
)

KEYCODES = (
    Keycode.UP_ARROW,    # GAS
    Keycode.DOWN_ARROW,  # BRAKE
    Keycode.LEFT_ARROW,  # LEFT
    Keycode.RIGHT_ARROW, # RIGHT
    Keycode.THREE,       # AK60
    Keycode.SPACE,       # POWER (placeholder - assign as needed)
)

keys = keypad.Keys(BUTTON_PINS, value_when_pressed=False, pull=True)

while True:
    event = keys.events.get()

    if event:
        key_idx = event.key_number

        if event.pressed:
            kbd.press(KEYCODES[key_idx])

            # Drift LED on BRAKE press
            if key_idx == 1:
                drift_led.value = True

        if event.released:
            kbd.release(KEYCODES[key_idx])

            if key_idx == 1:
                drift_led.value = False
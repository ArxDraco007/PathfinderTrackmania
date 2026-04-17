import board
import digitalio
import usb_hid
import keypad
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

kbd = Keyboard(usb_hid.devices)

BUTTON_PINS = (
    board.D0,  # GAS        
    board.D1,  # BRAKE          
    board.D2,  # LEFT       
    board.D3,  # RIGHT      
    board.D4,  # CHECKPOINT 
    board.D5,  # RESTART    
    board.D6,  # AK40       
    board.D7,  # AK60       
    board.D8   # AK80       
)

KEYCODES = (
    Keycode.UP_ARROW,    # GAS
    Keycode.DOWN_ARROW,  # BRAKE
    Keycode.LEFT_ARROW,  # LEFT
    Keycode.RIGHT_ARROW, # RIGHT
    Keycode.ENTER,       # CHECKPOINT (Respawn)
    Keycode.DELETE,      # RESTART (Give Up)
    Keycode.TWO,         # AK40 (TM default for 40% Action Key)
    Keycode.THREE,       # AK60 (TM default for 60% Action Key)
    Keycode.FOUR         # AK80 (TM default for 80% Action Key)
)

# 4. Setup Keypad array (Handles anti-bouncing automatically for E-sports speeds)
# pull=True uses the XIAO's internal pull-up resistors. 
# value_when_pressed=False because your KiCAD schematic connects switches to GND.
keys = keypad.Keys(BUTTON_PINS, value_when_pressed=False, pull=True)

# 5. Setup the Indicator LEDs
# POWER LED (KiCAD Pin 10 / GPIO4 / MISO)
power_led = digitalio.DigitalInOut(board.D9) 
power_led.direction = digitalio.Direction.OUTPUT
power_led.value = True  # Turn on immediately and stay on

# DRIFT INDICATOR LED (KiCAD Pin 11 / GPIO3 / MOSI)
drift_led = digitalio.DigitalInOut(board.D10)
drift_led.direction = digitalio.Direction.OUTPUT
drift_led.value = False # Starts off

# 6. Main Racing Loop
while True:
    event = keys.events.get() # Listen for button states
    
    if event:
        key_idx = event.key_number
        
        # When a button is PRESSED down
        if event.pressed:
            kbd.press(KEYCODES[key_idx])
            
            # If the BRAKE button (Index 1 in our list) is pressed, light up the Drift LED
            if key_idx == 1:
                drift_led.value = True
                
        # When a button is RELEASED
        if event.released:
            kbd.release(KEYCODES[key_idx])
            
            # If the BRAKE button is released, turn off the Drift LED
            if key_idx == 1:
                drift_led.value = False

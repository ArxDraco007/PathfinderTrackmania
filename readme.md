## Building a custom wireless TrackMania controller from scratch.

## Why did I make this project?
I started this as a cool starter project to test my understanding of hardware and electronics.
I wanted to make a controller solely dedicated to a game that is customizable and fully functional with the game. I chose TrackMania, it stuck to my heart, and I made this controller.
It is a split controller to make it ergonomic and handleable to play.

## Why does my project do?
It has movement and custom buttons, such as ak40, ak60, and ak80, which, when placed in calculated best locations, provide digital steering. On a keyboard, your keys are either "on" (100% steering) or "off" (0%). However, at high speeds or on certain surfaces, 100% steering can cause the car to slide out, lose grip, or slow down. Action Keys act like a limiter or a "virtual steering wheel" that holds the wheels at a precise angle.

## Zine - 
<img width="1304" height="1999" alt="zine (1)" src="https://github.com/user-attachments/assets/f3bf2800-09c4-43d9-91e2-239b12427a2c" />


## PICTURES - 
<img width="1315" height="854" alt="image" src="https://github.com/user-attachments/assets/09cdf43a-3613-40a5-accf-2165d3091dbe" />
<img width="1153" height="458" alt="image" src="https://github.com/user-attachments/assets/851f627e-cd24-4f55-9178-d86fa35b2d48" />

## How do you use it?

Just look at the control buttons and start playing! The WASD keys are on the right of the board, which correspond to the gas, left, brake, and right. The checkpoint and the reset buttons are below, and the AK40, AK60, and AK80 buttons, which control the full speed to 40, 60, and 80 percent. The AK60 is on the right. The AK40 and AK80 are on the  left.
Connect it using a USB to a PC.
Flash the firmware CircuitPython, copy code.py to the CIRCUITPY drive.
Game settings needed in TrackMania - enabling Action Keys 2/3/4.

### BOM

| Name               | Purpose                                  | Quantity | Total Cost (USD) | Link | Distributor |
|:-------------------|:-----------------------------------------|---------:|-----------------:|:-----|:------------|
| Custom PCB         | The PCB to hold all the components       | 10  | 7.00             | [Link](https://jlcpcb.com) | JLCPCB      |
| Blank DSA Keycaps  | Keycaps on top of the cherry mx          | 10       | 5.00             | [Link](https://meckeys.com/shop/accessories/keyboard-accessories/keycaps/blank-dsa-keycaps-1u/?srsltid=AfmBOoqZibFxneEDhpmnPoNkazQzsWt6AGt-IesHtl4qNnuvjoOs5HlY-7k) | meckeys |
| Cherry MX          | The keys for the pathfinder              | 1        | 5.00             | [Link](https://meckeys.com/shop/accessories/keyboard-accessories/key-switches/cherry-mx-rgb-switch/?srsltid=AfmBOorZoRj9h-qKXHVTCJLx7y5u4I8F4N70GPuj3bCzxEowvKHzzbSTq7I) | meckeys |
| SEEED XIAO RP2040  | The main board                           | 1        | 8.00             | [Link](https://robocraze.com/products/seeed-studio-xiao-rp2040-development-board?variant=47742255562976&country=IN&currency=INR&utm_medium=product_sync&utm_source=google&utm_content=sag_organic&utm_campaign=sag_organic&campaignid=23145906364&adgroupid=182236965810&keyword=&device=c&gad_source=1&gad_campaignid=23145906364&gbraid=0AAAAADgHQvZxlmp75q0W2JPaoE08GQ6we&gclid=Cj0KCQjwkYLPBhC3ARIsAIyHi3RSv8Y8s1jQFTQlRZ37opL-OW7Et0RKjRxRr56ogXQ1huokKAxQ5zoaAn2REALw_wcB) | Robocraze |
| **1.5V LED Bulbs** | Indication of Power and Drift. | 2 | 1 | [Link](https://www.amazon.in/UNIVERSAL-Multicolour-Yellow-Pieces-3v-3-2v/dp/B09RQRP81V/) | Amazon |
| Total | | | 26.00 | | |

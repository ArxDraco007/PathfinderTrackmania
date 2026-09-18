magnet:?xt=urn:btih:593A9E5577585AD6BCC4E3D4D993288AC5E2567D&dn=Spider-Man%20Brand%20New%20Day%202026%20V3%201080p%20TELESYNC%20x264-DKS&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337&tr=udp%3A%2F%2Fopen.stealth.si%3A80%2Fannounce&tr=udp%3A%2F%2Ftracker.torrent.eu.org%3A451%2Fannounce&tr=udp%3A%2F%2Ftracker.bittor.pw%3A1337%2Fannounce&tr=udp%3A%2F%2Fpublic.popcorn-tracker.org%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.dler.org%3A6969%2Fannounce&tr=udp%3A%2F%2Fexodus.desync.com%3A6969&tr=udp%3A%2F%2Fopen.demonii.com%3A1337%2Fannounce&tr=udp%3A%2F%2Fglotorrents.pw%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969&tr=udp%3A%2F%2Ftorrent.gresille.org%3A80%2Fannounce&tr=udp%3A%2F%2Fp4p.arenabg.com%3A1337&tr=udp%3A%2F%2Ftracker.internetwarriors.net%3A1337
## Building a custom wireless TrackMania controller from scratch.

## Why did I make this project?
I started this as a cool starter project to test my understanding of hardware and electronics.
I wanted to make a controller solely dedicated to a game that is customizable and fully functional with the game. I chose TrackMania, it stuck to my heart, and I made this controller.
It is a split controller to make it ergonomic and handleable to play.

## Why does my project do?
It has movement and custom buttons, such as ak40, ak60, and ak80, which, when placed in calculated best locations, provide digital steering. On a keyboard, your keys are either "on" (100% steering) or "off" (0%). However, at high speeds or on certain surfaces, 100% steering can cause the car to slide out, lose grip, or slow down. Action Keys act like a limiter or a "virtual steering wheel" that holds the wheels at a precise angle.

## Zine - 
<img width="1304" height="1999" alt="zine (2)" src="https://github.com/user-attachments/assets/56f66a9f-02df-4a47-8674-7f2fb01d180b" />


## PICTURES - 
<img width="1920" height="1080" alt="pathfindeee" src="https://github.com/user-attachments/assets/08fa5363-d715-465a-b30a-daae2fbbc022" />
<img width="1920" height="1080" alt="SnowPathfinder" src="https://github.com/user-attachments/assets/5eaaef70-4eaf-45d7-bb09-c7c1fc4fa58b" />
<img width="1920" height="1080" alt="DesertPathfinder" src="https://github.com/user-attachments/assets/c67acf3f-4165-4ea0-880e-91bb5830ed3b" />
<img width="1315" height="854" alt="image" src="https://github.com/user-attachments/assets/09cdf43a-3613-40a5-accf-2165d3091dbe" />
<img width="1153" height="458" alt="image" src="https://github.com/user-attachments/assets/851f627e-cd24-4f55-9178-d86fa35b2d48" />

## Assembly Instructions?
Heat-press the brass inserts into the case and glue the magnets into place.
Screw the stabilizers into the PCB and mount the sliding switch to the case.
Solder the diodes and header pins to the Seeeduino and PCB.
Click switches into the plate, screw the plate to the case, and add keycaps.
Flash your ZMK firmware to the Seeeduino.
Repeat for the second half, pair them, and test your work.

## How to use it?
Just look at the control buttons and start playing! The WASD keys are on the left of the board, which correspond to the gas, left, brake, and right. The checkpoint and the reset buttons are below, and the AK40, AK60, and AK80 buttons, which control the full speed to 40, 60, and 80 percent. The AK60 is on the left. The AK40 and AK80 are on the right.

### BOM

| Name               | Purpose                                  | Quantity | Total Cost (USD) | Link | Distributor |
|:-------------------|:-----------------------------------------|---------:|-----------------:|:-----|:------------|
| Custom PCB         | The PCB to hold all the components       | 10  | 7.00             | [Link](https://jlcpcb.com) | JLCPCB      |
| Blank DSA Keycaps  | Keycaps on top of the cherry mx          | 10       | 5.00             | [Link](https://meckeys.com/shop/accessories/keyboard-accessories/keycaps/blank-dsa-keycaps-1u/?srsltid=AfmBOoqZibFxneEDhpmnPoNkazQzsWt6AGt-IesHtl4qNnuvjoOs5HlY-7k) | meckeys |
| Cherry MX          | The keys for the pathfinder              | 1        | 5.00             | [Link](https://meckeys.com/shop/accessories/keyboard-accessories/key-switches/cherry-mx-rgb-switch/?srsltid=AfmBOorZoRj9h-qKXHVTCJLx7y5u4I8F4N70GPuj3bCzxEowvKHzzbSTq7I) | meckeys |
| SEEED XIAO RP2040  | The main board                           | 1        | 8.00             | [Link](https://robocraze.com/products/seeed-studio-xiao-rp2040-development-board?variant=47742255562976&country=IN&currency=INR&utm_medium=product_sync&utm_source=google&utm_content=sag_organic&utm_campaign=sag_organic&campaignid=23145906364&adgroupid=182236965810&keyword=&device=c&gad_source=1&gad_campaignid=23145906364&gbraid=0AAAAADgHQvZxlmp75q0W2JPaoE08GQ6we&gclid=Cj0KCQjwkYLPBhC3ARIsAIyHi3RSv8Y8s1jQFTQlRZ37opL-OW7Et0RKjRxRr56ogXQ1huokKAxQ5zoaAn2REALw_wcB) | Robocraze |
| **1.5V LED Bulbs** | Indication of Power and Drift. | 2 | 1 | [Link](https://www.amazon.in/UNIVERSAL-Multicolour-Yellow-Pieces-3v-3-2v/dp/B09RQRP81V/) | Amazon |
| M3x4 mm Brass Heat Set Threaded Round Insert Nut (25Pcs) | Metal screw threads to hold the plastic | 1 Pack | $4.00 | [View Product](https://robu.in/product/m3-x-4-mm-brass-heat-set-knurl-threaded-round-insert-nut-25-pcs/) | Robu |
| Total | | | 30.00 | | |

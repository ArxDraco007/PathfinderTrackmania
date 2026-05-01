# TrackManiaPathFinder
## Building a custom wireless TrackMania controller from scratch.

## Why did I make this project?
I started this as a cool starter project to test my understanding of hardware and electronics.
Although what I didn't see was the infinite potential this had, I started exploring what I could do with my Pathfinder.
I wanted to make a controller solely dedicated to a game that is customizable and fully functional with the game. I chose Hollow Knight, but that is for another day, as TrackMania stuck to my heart, and I made this controller.

## Why does my project do?
It has movement and custom buttons, such as ak40, ak60, and ak80, which, when placed in calculated best locations, provide digital steering. On a keyboard, your keys are either "on" (100% steering) or "off" (0%). However, at high speeds or on certain surfaces, 100% steering can cause the car to slide out, lose grip, or slow down. Action Keys act like a limiter or a "virtual steering wheel" that holds the wheels at a precise angle.

## PICTURES - 


![Screenshot 2026-04-17 170528](https://stasis.hackclub-assets.com/images/1776436253239-wztsvc.png)

![Screenshot 2026-04-17 170519](https://stasis.hackclub-assets.com/images/1776436252517-myqbl3.png)

## How do you use it?

Just look at the control buttons and start playing!

### BOM

| Name               | Purpose                                  | Quantity | Total Cost (USD) | Link | Distributor |
|:-------------------|:-----------------------------------------|---------:|-----------------:|:-----|:------------|
| Custom PCB         | The PCB to hold all the components       | 1        | 7.00             | [Link](https://jlcpcb.com) | JLCPCB      |
| Blank DSA Keycaps  | Keycaps on top of the cherry mx          | 2        | 5.00             | [Link](https://meckeys.com/shop/accessories/keyboard-accessories/keycaps/blank-dsa-keycaps-1u/?srsltid=AfmBOoqZibFxneEDhpmnPoNkazQzsWt6AGt-IesHtl4qNnuvjoOs5HlY-7k) | meckeys |
| Cherry MX          | The keys for the pathfinder              | 1        | 5.00             | [Link](https://meckeys.com/shop/accessories/keyboard-accessories/key-switches/cherry-mx-rgb-switch/?srsltid=AfmBOorZoRj9h-qKXHVTCJLx7y5u4I8F4N70GPuj3bCzxEowvKHzzbSTq7I) | meckeys |
| SEEED XIAO RP2040  | The main board                           | 1        | 8.00             | [Link](https://robocraze.com/products/seeed-studio-xiao-rp2040-development-board?variant=47742255562976&country=IN&currency=INR&utm_medium=product_sync&utm_source=google&utm_content=sag_organic&utm_campaign=sag_organic&campaignid=23145906364&adgroupid=182236965810&keyword=&device=c&gad_source=1&gad_campaignid=23145906364&gbraid=0AAAAADgHQvZxlmp75q0W2JPaoE08GQ6we&gclid=Cj0KCQjwkYLPBhC3ARIsAIyHi3RSv8Y8s1jQFTQlRZ37opL-OW7Et0RKjRxRr56ogXQ1huokKAxQ5zoaAn2REALw_wcB) | Robocraze |

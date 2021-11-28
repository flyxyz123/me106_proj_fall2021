# in development

## notes

software/electric to-do
- low priority
	- game logic?
		- store fastest time to complete game
	- crash sensor (switch) to flip control
	- resistors voltage divider for joystick ADC output? 
		- joystick seems need 5V input, and output range from 0 to 5V. Where pi pico ADC input highest is 3.3V, may need voltage divider for better input read.

machine to-do
- make laser more stable

## usage

arch linux with raspberry pi pico
```sh
paru -S adafruit-ampy micropython-git tio-git
# run from computer
sudo ampy -p /dev/ttyACM0 run main.py
# save to microcontroller
#sudo ampy -p /dev/ttyACM0 put main.py
# view output
sudo tio /dev/ttyACM0
```

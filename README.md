# in development

## notes

software/electric to-do
- high priority
	- photo resistor with laser
	- LCD display
- low priority
	- game logic?
		- score
	- joystick switch to start game
	- crash sensor (switch) to flip control
	- resistors voltage divider for joystick ADC output? 
		- joystick seems need 5V input, and output range from 0 to 5V. Where pi pico ADC input highest is 3.3V, may need voltage divider for better input read.
- maybe
	- state machine

machine to-do
- glue parts
- hole

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

# in development

## notes

software/electric to-do
- high priority
	- more sensors
		- sensor for detecting ball drop into the hole
			- crash sensor? like a switch, not count as one
	- display (LCD?)
- low priority
	- game logic?
		- score
	- find a use for joystick switch `joyk`
	- find datasheets
	- resistors voltage divider for joystick ADC output? 
		- joystick seems need 5V input, and output range from 0 to 5V. Where pi pico ADC input highest is 3.3V, may need voltage divider for better input read.
- maybe
	- state machine

machine to-do
- a lot 🙃

## usage

arch linux with raspberry pi pico
```sh
paru -S adafruit-ampy micropython-git
sudo ampy -p /dev/ttyACM0 run main.py
```

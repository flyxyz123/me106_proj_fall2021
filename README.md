# in development

## references

lcd code taken from:
- <https://github.com/Circuit-Digest/Raspberry_Pi_Pico_Tutorial/tree/main/T5_Interfacing_LCD/codes>
- <https://circuitdigest.com/microcontroller-projects/interfacing-raspberry-pi-pico-with-16x2-lcd-using-micropython>

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

## notes

improve
- more game logic
	- store fastest time to complete game
- resistors voltage divider for joystick ADC output? 
	- joystick seems need 5V input, and output range from 0 to 5V. Where pi pico ADC input highest is 3.3V, may need voltage divider for better input read.
- double photoresistor, one pointed by laser another one not, so no need to adjust threshold
	- how markets detect the laser?
- make laser more stable

from machine import Pin, ADC, PWM
from time import sleep_ms

PWM_MAX = (2**16)-1
# 2000 to 7000
DUTY_MIN = const(3500)
DUTY_MAX = const(5500)

servo0 = PWM(Pin(0))
servo1 = PWM(Pin(1))
servo0.freq(50)
servo0.freq(50)

hole = Pin(2, Pin.IN)
joyk = Pin(3, Pin.IN)

joyx = ADC(26)
joyy = ADC(27)

def servo_joy (servo, var):
    pos = (DUTY_MAX-DUTY_MIN)*var//PWM_MAX+DUTY_MIN
    servo.duty_u16(pos)
    print("pos", pos)
    sleep_ms(1)

while True:
    print("hole", hole.value())
    print("joyk", joyk.value())
    print("joyx", joyx.read_u16())
    print("joyy", joyy.read_u16())
    servo_joy(servo0, joyx.read_u16())
    servo_joy(servo1, joyy.read_u16())
    #sleep_ms(1)

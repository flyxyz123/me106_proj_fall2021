# lcd codes steal from 
# https://github.com/Circuit-Digest/Raspberry_Pi_Pico_Tutorial/tree/main/T5_Interfacing_LCD/codes
# https://circuitdigest.com/microcontroller-projects/interfacing-raspberry-pi-pico-with-16x2-lcd-using-micropython
import machine
import time

rs= machine.Pin(16,machine.Pin.OUT)
e = machine.Pin(17,machine.Pin.OUT)
d4 = machine.Pin(18,machine.Pin.OUT)
d5 = machine.Pin(19,machine.Pin.OUT)
d6 = machine.Pin(20,machine.Pin.OUT)
d7 = machine.Pin(21,machine.Pin.OUT)

def pulseE():
    e.value(1)
    #time.sleep_us(40)
    e.value(0)
    #time.sleep_us(40)

def longDelay(t):
    time.sleep_ms(t)

#def shortDelay(t):
#    time.sleep_us(t)

def send2LCD4(BinNum):
    d4.value((BinNum & 0b00000001) >>0)
    d5.value((BinNum & 0b00000010) >>1)
    d6.value((BinNum & 0b00000100) >>2)
    d7.value((BinNum & 0b00001000) >>3)
    pulseE()
    
def send2LCD8(BinNum):
    d4.value((BinNum & 0b00010000) >>4)
    d5.value((BinNum & 0b00100000) >>5)
    d6.value((BinNum & 0b01000000) >>6)
    d7.value((BinNum & 0b10000000) >>7)
    pulseE()
    d4.value((BinNum & 0b00000001) >> 0)
    d5.value((BinNum & 0b00000010) >> 1)
    d6.value((BinNum & 0b00000100) >> 2)
    d7.value((BinNum & 0b00001000) >> 3)
    pulseE()
    
def setCursor(line, pos):
    b = 0
    if line==1:
        b=0
    elif line==2:
        b=40
    returnHome()
    for i in range(0, b+pos):
        moveCursorRight()
    
def returnHome():
    rs.value(0)
    send2LCD8(0b00000010)
    rs.value(1)
    longDelay(2)

def moveCursorRight():
    rs.value(0)
    send2LCD8(0b00010100)
    rs.value(1)
    
def setupLCD():
    rs= machine.Pin(16,machine.Pin.OUT)
    e = machine.Pin(17,machine.Pin.OUT)
    d4 = machine.Pin(18,machine.Pin.OUT)
    d5 = machine.Pin(19,machine.Pin.OUT)
    d6 = machine.Pin(20,machine.Pin.OUT)
    d7 = machine.Pin(21,machine.Pin.OUT)
    rs.value(0)
    send2LCD4(0b0011)
    send2LCD4(0b0011)
    send2LCD4(0b0011)
    send2LCD4(0b0010)
    send2LCD8(0b00101000)
    send2LCD8(0b00001100)#lcd on, blink off, cursor off.
    send2LCD8(0b00000110)#increment cursor, no display shift
    send2LCD8(0b00000001)#clear screen
    #longDelay(2)#clear screen needs a long delay
    rs.value(1)
 
def displayString(row, col, input_string):
    setCursor(row,col)
    for x in input_string:
        send2LCD8(ord(x))
        time.sleep_ms(100)

def clearScreen():
    rs.value(0)
    send2LCD8(0b00000001)#clear screen
    #longDelay(2)#clear screen needs a long delay
    rs.value(1)

def servo_joy (servo, var):
    pos = (DUTY_MAX-DUTY_MIN)*var//PWM_MAX+DUTY_MIN
    #print("pos", pos)
    servo.duty_u16(pos)
    time.sleep_us(1)

joyk = machine.Pin(2, machine.Pin.IN)

PWM_MAX = const(65535)
# 2000 to 7000
DUTY_MIN = const(3000)
DUTY_MAX = const(6000)
DUTY_MID = const((DUTY_MIN+DUTY_MAX)//2)
PHOTO_THRESHOLD = const(44000)

servo0 = machine.PWM(machine.Pin(0))
servo1 = machine.PWM(machine.Pin(1))
servo0.freq(50)
servo1.freq(50)
servo0.duty_u16(DUTY_MID)
servo1.duty_u16(DUTY_MID)

joyx = machine.ADC(26)
joyy = machine.ADC(27)
photo = machine.ADC(28)

setupLCD()
clearScreen()
game = False
start_time=time.ticks_ms()
while True:
    print("photo", photo.read_u16())
    #print("joyx", joyx.read_u16())
    #print("joyy", joyy.read_u16())
    #print("game", game)
    if game == False and joyk.value() == 0:
        game = True
        start_time = time.ticks_ms()
        clearScreen()
    elif game == True and photo.read_u16() < PHOTO_THRESHOLD:
        game = False
        servo0.duty_u16(DUTY_MID)
        servo1.duty_u16(DUTY_MID)
    if game == True:
        displayString(1,0,str(time.ticks_ms()-start_time))
        servo_joy(servo0, joyx.read_u16())
        servo_joy(servo1, joyy.read_u16())
    time.sleep_ms(1)

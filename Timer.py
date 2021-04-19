import RPi.GPIO as GPIO
from    threading import Timer

def System_vidInit():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup( 2 , GPIO.OUT )
    GPIO.output(2 , GPIO.LOW)
    
    
LED_State = 0   

def ToggleLED():

    global LED_State
    
    if   LED_State == 0:
        GPIO.output(2 , GPIO.HIGH)
        LED_State = 1
        
    elif LED_State == 1:
        GPIO.output(2 , GPIO.LOW)
        LED_State = 0     
        
    else :
        pass
        
System_vidInit()
t = Timer(1 , ToggleLED)
t.start()

while True :
    pass
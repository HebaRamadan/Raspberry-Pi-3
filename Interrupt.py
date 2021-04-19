import RPi.GPIO as GPIO

def System_vidInit():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup( 2 , GPIO.OUT )
    GPIO.setup(3  , GPIO.IN    ,  pull_up_down=GPIO.PUD_UP)
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
GPIO.add_event_detect(3 , GPIO.RISING , callback = ToggleLED)

while True :
    pass
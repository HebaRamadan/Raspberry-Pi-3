import RPi.GPIO as GPIO

def Switch_vidInit(Switch_ID):
    GPIO.setmode(GPIO.BCM)
    
    #Initiate Switch PIN as INPUT PULL_UP
    GPIO.setup(Switch_ID , GPIO.IN , pull_up_down=GPIO.PUD_UP)
    
    
def Switch_u8GetValue(Switch_ID):
    Returned_Value =  GPIO.input(Switch_ID)
    
    return Returned_Value


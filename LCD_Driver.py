import RPi.GPIO as GPIO
import time


#Configure LCD PINS
LCD_RS   = 2
LCD_RW  = 3
LCD_EN   = 4

LCD_D0 =  21
LCD_D1 =  20
LCD_D2 =  16
LCD_D3 =  12
LCD_D4 =  7
LCD_D5 =  8
LCD_D6 =  25
LCD_D7 =  24

#DATA PINS of LCD on RPI
pins = [ LCD_D0 , LCD_D1 , LCD_D2 , LCD_D3 , LCD_D4 , LCD_D5 , LCD_D6 , LCD_D7 ]



def LCD_vidInit():

    GPIO.setmode(GPIO.BCM)
    
    #Initiate PINS as OUTPUT
    GPIO.setup( LCD_RS   , GPIO.OUT  )
    GPIO.setup( LCD_RW  , GPIO.OUT  )
    GPIO.setup( LCD_EN   , GPIO.OUT  )
    
    for PIN in pins :
        GPIO.setup( PIN  , GPIO.OUT  )
    
    #LCD_8BIT_2x16_5x7
    LCD_vidSendCommand(0x38)
    time.sleep(0.002)
    
    #Display_ON Cursor_OFF
    LCD_vidSendCommand(0x0C)
    time.sleep(0.002)
    
    #Clear Screen
    LCD_vidSendCommand(0x01)
    time.sleep(0.002)
        
    
    
    
    
def LCD_vidSendString(String) :     
    for Byte in String :
        LCD_vidSendData(Byte)
        
        
   
def LCD_vidClearScreen() : 
    LCD_vidSendCommand(0x01)
    time.sleep(0.002)
    
    
    
   
def LCD_vidSendCommand(COM) :
    
    #Select Write ON Command Register
    GPIO.output( LCD_RS  , GPIO.LOW)
    GPIO.output( LCD_RW , GPIO.LOW)
     
    #Write Command
    i = 0
    for PIN in pins :
        GPIO.output( PIN  , ((COM >> i)&(0x01))  )
        i += 1
    
    #Latch Signal ON EN PIN
    GPIO.output( LCD_EN  , GPIO.HIGH)    
    time.sleep(0.005) 
    GPIO.output( LCD_EN  , GPIO.LOW )
    
    
    
    
def LCD_vidSendData(CHAR) :   

    CHAR=ord(CHAR)
    
    #Select Write ON Data Register
    GPIO.output( LCD_RS  , GPIO.HIGH)
    GPIO.output( LCD_RW , GPIO.LOW )
        
    #Write Data
    i = 0
    for PIN in pins :
        GPIO.output( PIN  , ((CHAR >> i)&(0x01))  )
        i += 1
    
    #Latch Signal ON EN PIN
    GPIO.output( LCD_EN  , GPIO.HIGH)    
    time.sleep(0.005) 
    GPIO.output( LCD_EN  , GPIO.LOW )

import RPi.GPIO as GPIO

#Configure 7Segment Type
COM_Anode    = 0
COM_Cathode = 1
SevenSeg_Type  = COM_Cathode


#Configure 7Segment PINS
PIN0 =  2
PIN1 =  3
PIN2 =  4
PIN3 =  5
PIN4 =  6
PIN5 =  7
PIN6 =  8
PIN7 =  26

#PINS of 7Segment on RPI
pins = [ PIN0 , PIN1 , PIN2 , PIN3 , PIN4 , PIN5 , PIN6 , PIN7 ]

def SevenSeg_vidInit():
    global COM_Anode
    global COM_Cathode
    global SevenSeg_Type
    
    GPIO.setmode(GPIO.BCM)
    
    for PIN in pins :
        GPIO.setup( PIN  , GPIO.OUT  )
        
        if   SevenSeg_Type  == COM_Anode :
            GPIO.output(PIN  , GPIO.HIGH)
        elif SevenSeg_Type  == COM_Cathode :
            GPIO.output(PIN  , GPIO.LOW)    
        else :
            pass
        
def SevenSeg_vidDisplayNum(Number) :
    global COM_Anode
    global COM_Cathode
    global SevenSeg_Type

    if   SevenSeg_Type  == COM_Anode :
        Seg   = [0b11000000, 0b11111001, 0b10100100, 0b10110000, 0b10011001, 0b10010010, 0b0000010, 0b11111000, 0b10000000, 0b10010000]
    elif SevenSeg_Type  == COM_Cathode :
        Seg   = [0b00111111, 0b00000110, 0b01011011, 0b01001111, 0b01100110, 0b01101101, 0b01111101, 0b00000111, 0b01111111,0b01101111]
        
    temp =  Seg[Number]
    
    i = 0
    for PIN in pins :
        GPIO.output(PIN  , ((temp >> i)&(0x01)) )
        i += 1

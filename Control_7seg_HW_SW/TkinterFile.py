import tkinter
import RPi.GPIO as GPIO
from SevenSeg_Driver import  SevenSeg_vidDisplayNum
from Switch_Driver     import   Switch_u8GetValue

Switch_UP       = 20
Switch_Down   = 21

counter          = 0
Flag=0

def Init_Window():
    global Window 
    global Var_1
    global Flag
    global Button_1
    global Button_2
    Window = tkinter.Tk()
    Window.geometry("300x300")
    Window.title("SevenSeg_App")
    Window.resizable(width = "False" , height = "False")
    Window.configure(background="olive")
    i=0
    while i<10:
        Window.columnconfigure(i , minsize=20)
        Window.rowconfigure     (i , minsize=20)
        i+=1
        
    Button_1   =   tkinter.Button(Window , text = "UP"       , bg = "darkolivegreen" ,  fg = "black" , width = 10   , command = Tk_Count_UP   )
    Button_1.grid( row = 2 , column =  4   )

    Button_2   =   tkinter.Button(Window , text = "DOWN"  , bg = "darkolivegreen" ,  fg = "black" , width = 10   , command = Tk_Count_Down   )
    Button_2.grid( row = 4 , column =  4  )
    
    Button_3   =   tkinter.Button(Window , text = "HW"      , bg = "darkolivegreen" ,  fg = "black" , width = 10    , command=lambda:Check(1)  )
    Button_3.grid( row = 6 , column =  4  )
    
    Button_4   =   tkinter.Button(Window  , text = "Tkinter"  , bg = "darkolivegreen" ,  fg = "black" , width = 10   , command=lambda:Check(0)  )
    Button_4.grid( row = 8 , column =  4  )
    
    
def Check(x):
    global Flag
        
    if( x == 1) :
        Flag=1
    
    else :
        Flag=0


def HardwareFunction():
    global Switch_UP
    global Switch_Down
    global Switch_Tkinter
    
    GPIO.add_event_detect(Switch_UP,  GPIO.FALLING , callback = Hardware_Count_UP    )
    GPIO.add_event_detect(Switch_Down,  GPIO.FALLING , callback = Hardware_Count_Down)
    
    
    
        
def Hardware_Count_UP(Switch_UP):
    global Flag
    
    if Flag ==1:
        Count_UP()
    
    
    
    
def Hardware_Count_Down(Switch_Down):
    global Flag
    
    if Flag ==1:    
        Count_Down()
    
    
def Tk_Count_UP():
    global Flag
    
    if Flag ==0:
        Count_UP()
    
    
    
    
def Tk_Count_Down():
    global Flag
    
    if Flag ==0:    
        Count_Down()
    
    
    
    
def Count_UP():
    global counter 
    
    if counter < 9:
        SevenSeg_vidDisplayNum(counter)
        counter += 1    
    elif counter == 9:
        SevenSeg_vidDisplayNum(counter)
    else :
        pass
        

        
        
def Count_Down():
    global counter 
    
    if counter > 0:
        counter -= 1
        SevenSeg_vidDisplayNum(counter)
    elif counter == 0:
        SevenSeg_vidDisplayNum(counter)  
    else:
        pass

        

    
    

    

import tkinter
from SevenSeg_Driver import SevenSeg_vidDisplayNum

counter  = 0

def Init_Window():
    global Window 
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
        
        
def Create_Buttons():
    global Button_1
    global Button_2
    
    Button_1   =   tkinter.Button(Window , text = "UP"       , bg = "darkolivegreen" ,  fg = "black" , width = 10     , command = Count_UP   )
    Button_1.grid( row = 2 , column =  4   )

    Button_2   =   tkinter.Button(Window , text = "DOWN"  , bg = "darkolivegreen" ,  fg = "black" , width = 10    , command = Count_Down)
    Button_2.grid( row = 4 , column =  4  )
       

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
    
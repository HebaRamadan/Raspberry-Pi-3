import tkinter
from LCD_Driver import LCD_vidSendString
from LCD_Driver import LCD_vidClearScreen

counter  = 0

def Init_Window():
    global Window 
    Window = tkinter.Tk()
    Window.geometry("300x300")
    Window.title("LCD_App")
    Window.resizable(width = "False" , height = "False")
    Window.configure(background="olive")
    i=0
    while i<10:
        Window.columnconfigure(i , minsize=10)
        Window.rowconfigure     (i , minsize=10)
        i+=1
        
        
def Create_Buttons():
    global Entry_1
    
    Label_1     =   tkinter.Label(Window , text = "Please Enter Text :" , bg = "olive" ,  fg = "black")
    Label_1.grid(   row = 2 , column = 0    )
    
    Entry_1     =   tkinter.Entry(Window , width = 20)
    Entry_1.grid(   row = 3 , column = 0   )
    
    Button_1   =   tkinter.Button(Window , text = "Enter"       , bg = "darkolivegreen" ,  fg = "black" , width = 10     , command = WriteText   )
    Button_1.grid( row = 4 , column =  2   )

       

def WriteText():
    Text = Entry_1.get()
    LCD_vidClearScreen()
    LCD_vidSendString(Text)
    
    

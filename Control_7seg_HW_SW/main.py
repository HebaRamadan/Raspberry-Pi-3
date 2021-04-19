import TkinterFile
import  SevenSeg_Driver
import  Switch_Driver

Switch_UP       = 20
Switch_Down   = 21

SevenSeg_Driver.SevenSeg_vidInit()
Switch_Driver.Switch_vidInit(Switch_UP)
Switch_Driver.Switch_vidInit(Switch_Down)
Switch_Driver.Switch_vidInit(Switch_Tkinter)

TkinterFile.Init_Window()


TkinterFile.HardwareFunction()
TkinterFile.Window.mainloop()
    

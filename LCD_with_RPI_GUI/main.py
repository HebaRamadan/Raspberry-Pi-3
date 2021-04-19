import TkinterFile
import  LCD_Driver

LCD_Driver.LCD_vidInit()
TkinterFile.Init_Window()
TkinterFile.Create_Buttons()
TkinterFile.Window.mainloop()
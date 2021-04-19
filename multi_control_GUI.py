import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
from tkinter import * 



Motor_Pin = 2
Buzzer_Pin = 3
Led_Pin = 4

motor_state=0
buzzer_state=0
led_state=0

def motor_btn():
	global motor_state,Motor_Pin
	if motor_state == 0:
		GPIO.output(Motor_Pin,GPIO.HIGH)
		motor_state=1
		output.delete(0.0,END)
		output.insert(END,"Motor On")

		
	elif motor_state == 1:
		GPIO.output(Motor_Pin,GPIO.LOW)
		motor_state=0
		output.delete(0.0,END)
		output.insert(END,"Motor Off")
	
def buzzer_btn():
	global buzzer_state,Buzzer_Pin
	if buzzer_state == 0:
		GPIO.output(Buzzer_Pin,GPIO.HIGH)
		buzzer_state=1
		output.delete(0.0,END)
		output.insert(END,"Buzzer On")
		
	elif buzzer_state == 1:
		GPIO.output(Buzzer_Pin,GPIO.LOW)
		buzzer_state=0
		output.delete(0.0,END)
		output.insert(END,"Buzzer Off")

def led_btn():
	global led_state,Led_Pin
	if led_state == 0:
		GPIO.output(Led_Pin,GPIO.HIGH)
		led_state=1
		output.delete(0.0,END)
		output.insert(END,"Led On")
		
	elif led_state == 1:
		GPIO.output(Led_Pin,GPIO.LOW)
		led_state=0
		output.delete(0.0,END)
		output.insert(END,"Led Off")
	
GPIO.setup(Motor_Pin,GPIO.OUT)
GPIO.setup(Buzzer_Pin,GPIO.OUT)
GPIO.setup(Led_Pin,GPIO.OUT)

GPIO.output(Motor_Pin,GPIO.LOW)
GPIO.output(Buzzer_Pin,GPIO.LOW)
GPIO.output(Led_Pin,GPIO.LOW)	
		
main_window=Tk()
main_window.geometry("350x300+100+50")
main_window.title("##Multi device Control##")
main_window.configure(background ="black")	
motor_button=Button(main_window,text="Motor",width="14",font="none 18 bold",command=motor_btn)
motor_button.grid(row = 0, column = 3)
Button(main_window,text="Buzzer",width="14",font="none 18 bold",command=buzzer_btn).grid(row = 2, column = 3)
Button(main_window,text="Led",width="14",font="none 18 bold",command=led_btn).grid(row = 4, column = 3)
output = Text(main_window, width ="14",height='1', font = "none 18 bold", fg= "black", background="yellow")
output.grid(row = 6, column = 3)

main_window.mainloop()

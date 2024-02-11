from tkinter import *
import datetime
 
root = Tk()
root.geometry("600x600")
root.title("Arrival Times Tracker ")
root['bg']='#001118'
 
 #on button click function initialization
def Take_input():
    INPUT = inputtxt.get("1.0", "end-1c")
    
    REALTIME = datetime.datetime.now()
    #converting date & time from integer to a string for handling
    TIME = str(REALTIME)
    Output.insert(END, INPUT + " > AT : > ")
    Output.insert(END, "")
    Output.insert(END, TIME)
    Output.insert(END,"                   ")

##functionality works     
l = Label(text = "Enter the name", font=23, bg="#03a9f4")
inputtxt = Text(root, height = 2,
                font=25,
                width = 25,
                bg = "#0276ab")
 
Output = Text(root, height = 5, 
              width = 45, 
              font=17,
              bg = "#0276ab")
 
Display = Button(root, height = 2,
                 width = 20, 
                 font=11,
                 bg="#0276ab",
                 text ="ENTER",
                 command = lambda:Take_input())
 
l.pack()
inputtxt.pack()
Display.pack()
Output.pack()
 
mainloop()
from tkinter import *
 
root = Tk()
root.geometry("300x300")
root.title(" Q&A ")
 
def Take_input():
    INPUT = inputtxt.get("1.0", "end-1c")
    print(INPUT)
    import datetime
    REALTIME = datetime.datetime.now()
    TIME = str(REALTIME)
    Output.insert(END, INPUT + ">AT TIME>")
    Output.insert(END, "")
    Output.insert(END, TIME)
     
l = Label(text = "Enter ")
inputtxt = Text(root, height = 10,
                width = 25,
                bg = "light yellow")
 
Output = Text(root, height = 5, 
              width = 25, 
              bg = "white")
 
Display = Button(root, height = 2,
                 width = 20, 
                 text ="Show",
                 command = lambda:Take_input())
 
l.pack()
inputtxt.pack()
Display.pack()
Output.pack()
 
mainloop()
#Importing library.
import datetime
#Importing tkinter  GUI
from tkinter import *

#Entry initiation function
def printtext():
    global e
    #storing value of e.get into "string"
    string = e.get(); 
    #^prints the string
    print (string)

        #Concatecating and joining time and arivee variables.
    

    #Opening the logs.txt file to write, 'a' argument to continue on to already written file.
        ##openlogs = open('logs.txt', 'a')
    #Actually writing into the file, from the info variable we made earlier.
        ##openlogs.write(info)

    #Assigning time to a variable.
        ##time = datetime.datetime.now()

#Converting realtime output into a string for further processing.
        ##realtime = str(time)
root = Tk()
e = Entry(root)
e.pack()
e.focus_set()

root.geometry('400x200')

##This is button funcitonality
#When we click, we want to store text 
#from input box to .txt file
#our entry() function does that already
#maybe we could call it.
#We called it but it gets called on button event, and -expects prompt in the console-

    
#Assigning time to a variable.
#time = datetime.datetime.now()

#Converting realtime output into a string for further processing.
#realtime = str(time)


##entry1 = Entry(root, width=20)entry1.pack()

Button(root, text="Enter user", command=printtext).pack()

root.mainloop()

######################################################
    




    
    


    
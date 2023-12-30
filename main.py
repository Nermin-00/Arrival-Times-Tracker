#Importing library.
import datetime

#Assigning time to a variable.
time = datetime.datetime.now()

#Converting realtime output into a string for further processing.
realtime = str(time)

##Deciding between multiple user input during runtime.
multipleUserInput = input("Multiple User Entry? Y/N ")
if (multipleUserInput == "N" ):
    print(" No multiple entry activated.")
     #Prompting for arivee's name.
    arivee = input("Enter who arrived : ")

    #Concatecating and joining time and arivee variables.
    info = arivee + " - " + realtime + "\n"

    #Opening the logs.txt file to write, 'a' argument to continue on to already written file.
    openlogs = open('logs.txt', 'a')
    #Actually writing into the file, from the info variable we made earlier.
    openlogs.write(info)
    
##Multiple User Entry during runtime functionality. 
else:
    print("Multiple User Entry Mode Activated!")
    multipleEntry = input("Enter the amount of arivee's you'd like to add : ")
    print("Converting string to int data type")
    multipleEntryInt = int(multipleEntry)
    print("Supposed to evaluate")
if (multipleEntryInt == 1):
    print("IIIII")
    print("Invalid, single user entry detected.")
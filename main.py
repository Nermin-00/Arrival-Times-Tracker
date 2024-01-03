#Importing library.
import datetime

#Entry initiation function
def entry():
    
        arivee = input("Enter who arrived : ")

    #Concatecating and joining time and arivee variables.
        info = arivee + " - " + realtime + "\n"

    #Opening the logs.txt file to write, 'a' argument to continue on to already written file.
        openlogs = open('logs.txt', 'a')
    #Actually writing into the file, from the info variable we made earlier.
        openlogs.write(info)

#Assigning time to a variable.
time = datetime.datetime.now()

#Converting realtime output into a string for further processing.
realtime = str(time)


##Deciding between multiple user input during runtime.
multipleUserInput = input("Multiple User Entry? Y/N ")
if (multipleUserInput == "N" ):
    print(" No multiple entry activated.")
     #Prompting for arivee's name, function call.
    entry()
    
    
#Multiple User Entry during runtime functionality. 
else:
    print("Multiple User Entry Mode Activated!")
    multipleEntry = input("Enter the amount of arivee's you'd like to add : ")
    #Converting string into an int.
    multipleEntryInt = int(multipleEntry)
    
#Calling the function the amount of times entered during Multiple User Entry
for x in range (multipleEntryInt):
    print(x)
    entry()
    
    
    
    
    


    
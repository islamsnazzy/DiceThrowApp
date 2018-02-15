from random import *
        
def prompt():
    userInput = input("do you want to throw? press 'y' to start and 'n' to stop: ")
    while userInput ==' ':
        userInput = input("do you want to throw? press 'y' to start and 'n' to stop: ")

    if userInput == 'y':
        print(randint(1,6))    
    else:
        return "game over"

    toContinue = input("do you want to continue to throw? press 'y' to continue and 'n' to stop: ").lower()
    if toContinue == 'y':
         print(prompt())
    else:
        return "end of programme!!"
    
prompt()



    

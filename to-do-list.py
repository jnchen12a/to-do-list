#Creating to-do list
unfinished = []
completed = []

#Function that prints out full to-do list
def show_tdlist():
    print("To-Do:")
    for item in unfinished:
        print(" - " + item)
    print()
    print("Completed:")
    for item in completed:
        print(" - " + item)
    print()

#Seeing if user is worthy of using this program
while True:
    response1 = input("Are you ready to be productive today?")
    try:
        response1 = response1.lower()
    except:
        print("What? Try again.")
        continue
    
    if response1 == "yes":
        print("Nice! Let's get started!")
        break
    elif response1 == "no":
        print("Okay, sounds good. Have fun loafing around.")
        quit()
    else:
        print("What? Try again.")

#Entering first item on to-do list
firstitem = input("What is the first item on your to-do list?")
firstitem = firstitem.capitalize()
unfinished.append(firstitem)
show_tdlist()
print("Looking good so far!")

#Loop to add or complete tasks on list
while True:
    #Asks question and gets input
    print("What would you like to do next?")
    print("Would you like to add a task, complete a previous one, or quit out?")
    decision = input("Please type add, complete, or quit.")

    #Bozo check
    try:
        decision = decision.lower()
    except:
        print("Sorry, that makes absolutely no sense. Please type add, complete, or quit.")
        continue
    
    #if else statement that uses input
    if decision == "add": #adding a task
        newitem = input("What task would you like to add?")
        unfinished.append(newitem)
        show_tdlist()
    elif decision == "complete":
        #Stuff
    elif decision == "quit": #quiting out of program
        print("Thank you for using this program! Three cheers to you for being productive today!")
        quit()
    else: #Bozo check again
        print("Sorry. Please type add, complete or quit.")
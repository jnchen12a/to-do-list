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
    if len(completed) == 0:
        print("None (yet)")
    else:
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
        newitem = newitem.capitalize()
        if newitem in unfinished:
            print("Sorry, that item is already there.")
            show_tdlist()
            continue
        unfinished.append(newitem)
        show_tdlist()
    elif decision == "complete": #completing a task
        if len(unfinished) == 0:#Bozo check
            print("Sorry. There seems to be no tasks to complete, but that might be a good thing.")
            continue

        print("Congratulations! Which task did you complete?")

        #Lists out all unfinished tasks
        for item in unfinished:
            tasknumber = unfinished.index(item) + 1
            tasknumberstr = str(tasknumber)
            print(tasknumberstr + ". " + item)

        #Asks which one was completed
        while True:
            completedtaskn = input("Please enter the number corresponding to the task you completed or type 0 to return to the previous menu.")
            try:
                completedtaskn = int(completedtaskn)
            except:
                print("Please enter a number. Try again.")
                continue
            
            #if else statement to decide what to do next
            if completedtaskn == 0: #return to previous menu
                break
            elif completedtaskn > len(unfinished): #Bozo check
                print("That task doesn't exist yet. Try again.")
                continue
            else: #Move task from unfinished to completed list
                completedtaskn = completedtaskn - 1
                movingtask = unfinished[completedtaskn]
                del unfinished[completedtaskn]
                completed.append(movingtask)
                print("Nice! That task has been officially completed!")
                show_tdlist()
                break
    elif decision == "quit": #quiting out of program
        print("Thank you for using this program! Three cheers to you for being productive today!")
        quit()
    else: #Bozo check again
        print("Sorry. Please type add, complete or quit.")
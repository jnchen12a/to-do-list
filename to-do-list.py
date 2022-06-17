#Creating to-do list
unfinished = []
completed = []

#Function that prints out full to-do list
def show_tdlist():
    print("To-Do:")
    if len(unfinished) == 0:
        print("None (Let's go!)")
    else:
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
    
    if response1 == "yes" or response1 == "yes!":
        print("Nice! Let's get started!")
        break
    elif response1 == "no":
        print("Okay, sounds good. Have fun loafing around.")
        quit()
    else:
        print("What? Try again.")

#Asking user to create new list or import an existing one
while True:
    newimportres = input("Would you like to\n 1. Create a new to-do list\n 2. Import an existing one, or\n 3. Quit out of this program?")
    
    #Bozo check
    try:
        newimportres = int(newimportres)
    except:
        print("Sorry. Please enter 1, 2, or 3.")
        continue
    
    if newimportres == 1: #Creating new to-do list
        #Entering first item on to-do list
        firstitem = input("Great! What is the first item on your to-do list?")
        firstitem = firstitem.capitalize()
        unfinished.append(firstitem)
        show_tdlist()
        print("Looking good so far!")
        break
    elif newimportres == 2: #Importing old list
        while True:
            print('Please paste your existing to-do list here, with different items seperated by a "-".')
            importlist = input("If you'd like to quit out, please type quit.")
            #Bozo Check
            try:
                importlist = importlist.lower()
            except:
                print("Sorry, something went wrong. Please try again.")
                continue
            if importlist == "quit": #Quiting out
                print("Thank you for using this program.")
                quit()
            else: #Trying to import list
                if "-" not in importlist: #User didn't import a list
                    print('Sorry, please seperate your items with a "-" and try again.')
                    continue
                else: #Spliting input string
                    importlist = importlist.split("-")
                    importlist.remove(importlist[0])
                    for item in importlist:
                        unfinished.append(item)
                    show_tdlist()
                    print("Does that look right?")
                    while True:
                        importcheck = input("Please type yes or no.")
                        try:
                            importcheck = importcheck.lower()
                        except:
                            print("Sorry, something went wrong. Please try again.")
                            continue
                        if importcheck == 'yes':
                            print("Great!")
                            break
                        elif importcheck == 'no':
                            print("Sorry. Please check your list and try again.")
                            unfinished = []
                            break
                        else:
                            print("Sorry, something went wrong. Please try again.")
                            continue
                    break
        #End of while loop?
        break
    elif newimportres == 3: #Quiting out
        print("Thank you for using this program.")
        quit()
    else: #Bozo check
        print("Sorry. Please enter 1, 2, or 3.")
        continue


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
        if len(completed) == 0:
            print("Thank you for using this program!")
        else:
            print("Thank you for using this program! Three cheers to you for being productive today!")
        print()
        print("Here are your stats for today:")
        print("Number of unfinished tasks: " + str(len(unfinished)))
        print("Number of completed tasks: " + str(len(completed)))
        if len(unfinished) > 0:
            print()
            print("***NOTICE***")
            print("You still have some unfinished tasks. Make sure you complete them later!")
            print("************")
        print()
        print("Please give Jason Chen a high-five the next time you see him\nto let him know what a great job he did on this program!")
        quit()
    else: #Bozo check again
        print("Sorry. Please type add, complete or quit.")
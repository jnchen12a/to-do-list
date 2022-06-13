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

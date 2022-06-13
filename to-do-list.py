#Creating to-do list
tdlist = []
unfinished = []
completed = []
tdlist.append(unfinished)
tdlist.append(completed)

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

firstitem = input("What is the first item on your to-do list?")
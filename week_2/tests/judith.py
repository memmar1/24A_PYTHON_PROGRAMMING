option = ""


while True:
    option = input("")
    if option == "start":
        started = True
        if started:
            print("The car is already started")
        else:
            started = False
            print ("start the car")
    elif option == "stop":
        print("Stop the car!")
    elif option == "quit":
        break
    elif option == "help":
        print("""
            start - to start the car
            stop - to stop the car
            quit - to exit the game
        """)
    else:
        print("I dont get it...")
#Random Number guesser Game!

def Number_Guess():
    import random
    #This is a variable that will be used to generate a random number
    number = random.randint(0,100)
    #This is a variable that will be used to give the user tries
    tries = 10
    #'while' will be used to keep a loop gong
    while tries > 0: #if tries reach 10 it will stop the loop
        #This is a variable that will store the user input
        Guessed = int(input(f"You have {tries} left, guess the number: "))
        #'if' will be used to check the user guess if its the same
        if Guessed == number:
            #This will print that the user has entered the correct number
            print("Correct! You guessed the number!")
            #this will ask the user if he wants to play again
            User_Play = input("If you want to play again please enter yes! : ")
            #This will check if the user as inputted yes if the user did it will continue else it will break the loop
            if User_Play == "yes":
                tries = 10
                continue
            else:
                break
            #This will check if the user input is wrong
        else:
            #This will print that the user guessed wrong
            print("Wrong! Try again")
            #This will take away a try
            tries -= 1
            #This will check if tries is 0
            if tries == 0:
                #this will ask the user if he wants to play again
                User_Play = input("If you want to play again please enter yes! : ")
                #This will check if the user as inputted yes if the user did it will continue else it will break the loop
                if User_Play == "yes":
                    tries = 10
                    continue
                else:
                    break
            #This will continue if Tries is not 0
            continue
Number_Guess()
            

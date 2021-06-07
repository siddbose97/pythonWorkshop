import random

def rps():
    myScore = 0 #our score
    computerScore = 0 #computer's score

    keepPlaying = True #do we want to keep playing?

    while keepPlaying == True: #if we want to keep playing, then keep looping
        playerChoice = input("Make a choice: rock, paper or scissors - ")#the input string
        
        if playerChoice != "rock" and playerChoice != "paper" and playerChoice != "scissors": #check input
            print("Input is invalid: please input rock, paper or scissors. Max 3 Wrong Inputs") #tell player what's wrong
            badInputCounter = badInputCounter + 1 #increment bad input counter
            if badInputCounter >= 3: #if 3 bad inputs in a row, leave the game
                print("3 Mistakes, Goodbye")
                break 
            else: #if less than 3 wrong entries, then report how many wrong and continue
                output = "You have made this many wrong inputs in a row: " + str(badInputCounter) 
                print(output)
                continue

        computerChoice = random.randrange(1,3) #let the computer randomly choose 1, 2, or 3
        computerMappedChoices = {1:"rock", 2:"paper", 3:"scissors"} #let's convert a number to a choice
        computerChoiceString = computerMappedChoices[computerChoice] #plug the random number into the dictionary    

        badInputCounter = 0 #reset bad input counter whenver a good input is given

        if computerChoiceString == playerChoice: #if choices are same, then Tie
            result = "Player: " + playerChoice + " and Computer: " + computerChoiceString + " = Tie"
            myScore = myScore + 1 #update player and computer score
            computerScore = computerScore + 1
            print(result)
            ScoreString = "Score is now " + str(myScore) + " for player and " + str(computerScore) + " for Computer!"
            print(ScoreString) #print the new score

        elif (computerChoiceString == "rock" and playerChoice == "paper") or (computerChoiceString == "paper" and playerChoice == "scissors") \
        or (computerChoiceString == "scissors" and playerChoice == "rock"): #check all win conditions and update score
            
            result = "Player: " + playerChoice + " and Computer: " + computerChoiceString + " = Player Wins!"
            myScore = myScore + 1 #update player score
            print(result)
            ScoreString = "Score is now " + str(myScore) + " for player and " + str(computerScore) + " for Computer!"
            print(ScoreString) #print the new score

        else: #if not a tie or player did not win, then by definition, computer must win! lets save some code this way
            result = "Player: " + playerChoice + " and Computer: " + computerChoiceString + " = Computer Wins!" 
            computerScore = computerScore + 1 #update computer score
            print(result)
            ScoreString = "Score is now " + str(myScore) + " for player and " + str(computerScore) + " for Computer!"
            print(ScoreString) #print the new score

        checkIn = input("Do you want to keep playing: if yes, press any key, if no, type: no - ") #ask if want to keep playing
        
        if checkIn == "no": #check for response
            keepPlaying = False #set boolean to False: since loop only continues on True, this breaks the loop
        else:
            continue
    
rps()

    
    
    

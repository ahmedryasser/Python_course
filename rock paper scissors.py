print (" Welcome to Rock Paper Scissors ")
print(" ")
tryagain = "yes"

name1 = input(" Player 1, what is your name? ")
name2 = input(" Player 2, what is your name? ")





while tryagain == "yes" or tryagain == "Yes" :
    p1 = input( name1 + ", What do you choose ")
    p2 = input( name2 + ", What do you choose ")

    if p1 == "rock" or p1 == "Rock" and p2 == "scissors" or p2 == "Scissors":
        print (name1 + " wins ")

    elif p1 == "paper" or p1 == "Paper" and p2 == "rock" or p2 == "Rock" :
        print (name1 + " wins ")

    elif p1 == "scissors" or p1 == "Scissors" and p2 == "paper" or p2 == "Paper":
        print (name1 + " wins ")

    elif p2 == "rock" or p2 == "Rock" and p1 == "scissors" or p1 == "Scissors":
        print (name2 + " wins ")

    elif p2 == "paper" or p2 == "Paper" and p1 == "rock" or p1 == "Rock":
        print (name2 + " wins ")

    elif p2 == "scissors" or p2 == "Scissors" and p1 == "paper" or p1 == "Paper":
        print (name2 + " wins ")

    elif p2 == "rock" or p2 == "Rock" and p1 == "rock" or p1 == "Rock":
        print (" It's a tie ")

    elif p2 == "paper" or p2 == "Paper" and p1 == "paper" or p1 == "Paper":
        print (" It's a tie ")

    elif p2 == "scissors" or p2 == "Scissors" and p1 == "scissors" or p1 == "Scissors":
        print (" It's a tie ")

    else:
        print (" Invalid entry ")
    tryagain = input(" Would you like to try again")

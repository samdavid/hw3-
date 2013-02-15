# Copywrite 2013 Samuel Christian
# Homework Assignment 3
# Penny Matching

# In the game, the computer tries to guess what the player has chosen
# heads or tails. When the computer gueses correctly, it gets a penny.
# When it is incorrect, the player receives a penny.
# After 10 rounds, whoever has the most pennies is the winner

import random
roundNum = 0
playerchoice = ""
scoreComp = 0
scorePl = 0

name = input("Welcome! What is your name? ")
print("")
for i in range(10):
    roundNum += 1
    compchoice = random.randint(0,15) #Computer's quess
    if compchoice <= 7:
        guess = "heads"
    elif compchoice > 7:
        guess = "tails"
        
    print("--- Round", roundNum, "---") #Round begins
    print(name, end = ", ")
    input("secretly choose heads or tails and then press <enter>")
    print("I guess you chose:", guess)   
    playerchoice = input("What did you pick, heads(h) or tails(t)? ")
    while playerchoice != "h" and playerchoice != "t":
        playerchoice = input("Sorry, please enter 'h' or 't'. ")

    if playerchoice == guess[0]:
        print("One penny for me!")
        scoreComp += 1
    else:
        print("One penny for", name)
        scorePl += 1
    print("")

print("--- Final score --- ")
print("Computer:",scoreComp)
print(name,":", scorePl)
if scoreComp > scorePl:
    print("I win!")
elif scoreComp < scorePl:
    print("You win!")
elif scoreCom == scorePl:
    print("Tie!")

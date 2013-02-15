import random
roundNum = 0

for i in range(3):
    roundNum += 1
    compchoice = random.randint(0,15)
    if compchoice <= 7:
        guess = "Heads"
    elif compchoice > 7:
        guess = "Tails"
    print("Round", roundNum, "start!")
    print("")
    print("Player: secretly choose heads or tails and then press <enter>")
    print("My guess is:", guess, "!")   

    print("")

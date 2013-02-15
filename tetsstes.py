import random

for i in range(10):
    compchoice = random.randint(0,15) #Computer's quess
    if compchoice <= 7:
        guess = "heads"
    elif compchoice > 7:
        guess = "tails"
    print(guess[0])

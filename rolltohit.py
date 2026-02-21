#This simulates rolling to hit in Warhammer 40,000
#Prompt the user how many dice are being rolled, and what the hit target is
#Roll the correct number of dice, then display the results
#This is a guided practice. Either follow with the video or your instructor will
#go over this in class.

import random

random.seed()

diceCount = int(input("How many dice to be rolled: "))
hitTarget = int(input("What is the hit target: "))

hitCount = 0
diceRoll = 0

for i in range(diceCount):
    diceRoll = random.randint(1,6)
    print(f"Roll is {diceRoll}.")
    if diceRoll >= hitTarget:
        hitCount += 1

print(f"{diceCount} dice were rolled with a hit target of {hitTarget}, and it hit {hitCount} times.")
# Project --> Number Guessing Game

import random
print("\t Number Guessing Game")

n = random.randint(1,100)
a = -1
gusses = 0
while(a != n):
    gusses += 1
    a = int(input("Enter number:"))
    if(a>n):
        print("Lower number please.")
    elif(a==n):
        break
    else:
        print("Higher number please.")
print(f"You have gussed the number correctly in {gusses} attempts.")


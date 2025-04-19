
# Ye hamara main project hi h bs isme logic lga ke ise short kr diya gya h, mtlb logic ko hi
# short m likh diya h 

import random
computer = random.choice([-1,1,0]) # ye vo function h jha pr hum random function or method use kr rhe h.
youstr = input("Enter your choice: ")
game = {
    "R" : 1,  #Snake
    "P" : -1, #Gun
    "S" : 0 #Water
}
reversedict = {
    1 : "Rock",
    -1 : "Paper",
    0 : "Scissor"
}
you = game[youstr]

print(f"You chose {reversedict[you]} \nComputer chose {reversedict[computer]}")

'''
if(computer==you):
    print("Game Draw")
else:    
    if(computer == -1 and you ==0): --> -1-0 = -1 (Win)
        print("You Win!")

    elif(computer==-1 and you==1): --> -1-1 = -2 (Lose)
        print("You Lose!")

    elif(computer==1 and you==-1): --> 1-(-1) = 2 (Win)
        print("You Win!")

    elif(computer==1 and you==0):  --> 1-0 = 1 (Lose)
        print("You Lose!")

    elif(computer==0 and you==1):  --> 0-1 = -1 (Win)
        print("You Win!")

    elif(computer==0 and you==-1): --> 0-(-1) = 1 (Lose)
        print("You Lose!")
    else:
        print("Something went Wrong.")

Logic --> Yha Pr basically Lose tb aa rha h jb (1) ho ya fr jb (-2) ho tb.
      Like [(computer - you) = 1 h agr to lose or agr -2 bhi h to bhi lose. Nhi to Win.]
'''




if((computer -you) == 1 or (computer-you)==-2):
    print("You Lose!")
else:
    print("You Win!")
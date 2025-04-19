# Yha pr chatgpt ko use krke program ko asani se bnaya ja skta h, generally jo functions ya other 
# things jo hame pta nhi hote, hum chatgpt ka use krke asani se kr skte h.
# Chatgpt --> Increases working productivity.

import random  # Ise isliye import kiya taki random choice m se chose ho by computer.
'''
Rock -> 1 --> Rock breaks scissor but not scissor.
Paper -> -1 --> Paper slows down rock, but not scissor.
Scissor -> 0 --> Scissor can cut Paper, but not rock.

'''
computer = random.choice([-1,1,0]) # ye vo function h jha pr hum random function or method use kr rhe h.
print("Choose following:"
      "Rock --> R\n"
      "Paper --> P\n"
      "Scissor --> S")
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

if(computer==you):
    print("Game Draw")
else:    
    if(computer == -1 and you ==0):
        print("You Win!")

    elif(computer==-1 and you==1):
        print("You Lose!")

    elif(computer==1 and you==-1):
        print("You Win!")

    elif(computer==1 and you==0):
        print("You Lose!")

    elif(computer==0 and you==1):
        print("You Win!")

    elif(computer==0 and you==-1):
        print("You Lose!")
    else:
        print("Something went Wrong.")


# Project --> Simple ATM System.    
                        # !!!Incompleted

def ATM():
    Acc_Bal = 50000
    Pin = 1234

    pin = int(input("Enter Pin: "))
    
    if pin == Pin:
        while True:
            print("\n1. Balance Inquiry")
            print("2. Deposit")
            print("3. Withdrawl")
            print("4. Exit")

            choice = int(input("Enter your Choice: "))
            if choice == 1:
                print(f"Your Balance is {Acc_Bal}")
            elif choice ==2:
                deposit_amount = int(input("Enter Deposit Amount: "))
                Acc_Bal += deposit_amount
                print(f"Deposited = {deposit_amount}. New Balance is {Acc_Bal}")
            elif choice == 3:
                withdrawl_amount = int(input("Enter Withdrawl Amount: "))

                with_bal = Acc_Bal
                with_bal -= withdrawl_amount
                if(withdrawl_amount<=Acc_Bal):
                    print(f"Withdrawl Amount = {withdrawl_amount}. Balance is {with_bal}")
                else:
                    print("Insufficent Balance.")
                    
            elif choice == 4:
                break
            else:
                print("Invalid Input")
    else: 
        print("Incorrect Password")


ATM()
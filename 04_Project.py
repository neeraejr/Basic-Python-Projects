# Basic Banking System

def AccountCreation():
    print("Personal Details\n")
    f_name = input("First Name: ")
    l_name = input("Last Name: ")
    name = f_name + l_name
    print(f"Full Name: {name}")
    DOB = input("Date of Birth: ")
    AddPer = input("Permanent Address: ")
    AddCur = input("Current Address: ")
    PhNo = int(input("Phone Number: "))
    Email = input("Email: ")
    print("\n")

    print("Identification Details\n")
    
    # Acc_No = int(input("Account Number: "))


AccountCreation()
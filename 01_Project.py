# Simple Calculator

def Calculator():
    while True:
        operation = input("Choose Add for Addition, Sub for Substraction, Mul for Multicplication,"
                          "Div for Division and Rem for Remainder And exit to quit: ")
        if operation.lower() == "add":
            n = int(input("Enter number for inputs: "))
            sum = 0
            for i in range(0,n):
                num1 = int(input("Enter number: "))
                sum = sum+num1
            print(f"Sum of {n} numbers is: {sum}")

        elif operation.lower() == "sub":
            n = int(input("Enter number for inputs: "))
            num1 = int(input("Enter number: "))
            for i in range(1,n):
                nextnum = int(input("Enter number: "))
                num1 -= nextnum
            print(f"Difference of {n} numbers is: {num1}")

        elif operation.lower() == "mul":
            n = int(input("Enter number for inputs: "))
            mul = 1
            for i in range(0,n):
                num1 = int(input("Enter number: "))
                mul = mul*num1
            print(f"Multiplication of {n} numbers is: {mul}")

        elif operation.lower() == "div":
            try:
                num1 = float(input("Enter 1st number: "))
                num2 = float(input("Enter 2nd number: "))
                Div = num1/num2
                print(f"Division of these numbers is: {Div}")
            except ZeroDivisionError:
                print("Division by Zero not Possible.")

        elif operation.lower() == "rem":
            num1 = float(input("Enter 1st number: "))
            num2 = float(input("Enter 2nd number: "))
            Remain = num1%num2
            print(f"Remainder of these numbers: {Remain}")

        elif operation.lower() == "exit":
            break
        else:
            print("Invalid Input, Please Try again.")

Calculator()
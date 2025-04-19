# Program of Simple calculator.
import math   #Math module for mathematics calculations.


class CalulateAddSub:
    #For addition, Substraction, Multiplication and Divide.
    def calcu(self):
        while True:
            operation = input("Choose 'OP' for performing operation and 'exit' to quit: ")
            if operation.lower() == 'op':
                expression = input("Enter the expression: ")
                try:
                    result = eval(expression)
                    print("Result: ", result)
                except Exception as e:
                    print("Error in expression: ",e)
            elif operation.lower() == 'exit':
                break
            else:
                print("Invalid Input, Please Enter correct values for Performing Operations.")
    
class AdvanceCalculation(CalulateAddSub):
    def Adcalcu(self):
        while True:
            operation = input("Choose an operation - power (^), squareroot(sqr), modulus(%), or 'exit' to quit: ")
            if operation.lower() == '^':
                base = float(input("Enter base: "))
                exponent = float(input("Enter exponent: "))
                result = base**exponent
                print(f"{base} power {exponent} is: ",result)
            elif operation.lower() == 'sqr':
                number = float(input("Enter number: "))
                if number<0:
                    print("Square root of negative no. is not defined.")
                else:
                    result = math.sqrt(number)
                    print(f"Square root of √{number} is: ",result)
            elif operation.lower() == '%':
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                try:
                    result = num1%num2
                    print("Remainder afer divison is: ",result)
                except Exception as e:
                    print("Division by zero is not Allowed")
            else:
                print("Invalid Operation. Please try again later.")

class LogarithmicOperations(AdvanceCalculation):
    def loga(self):

        while True:
            operation = input("Choose an operation - natural log(ln), log base 10 (log), or 'exit' to quit: ")
            if operation.lower() == 'exit':
                break
            elif operation.lower() == 'ln':
                number = float(input("Enter number for Natural Log: "))
                if (number<0):
                    print("Logarithms is not defined for non-positive numbers")
                else:
                    result = math.log(number)  #For Natural Log using math module.
                    print(f"Natural Log of {number} is: ",result)
            elif operation.lower() == 'log':
                number = float(input("Enter number for Log Base 10: "))
                if (number<0):
                    print("Logarithms is not defined for non-positive numbers")
                else:
                    result = math.log10(number)  #For Natural Log using math module.
                    print(f" Log Base 10 of {number} is: ",result)

class Factorial(LogarithmicOperations):
    def Fact(self):
        while True:
            operation = input("Enter a non negative integer for factorail or 'exit' to quit: ")

            if operation.lower() == 'exit':
                break
            try:
                num = int(operation)
                if num<0:
                    print("Factorail is not defined for negative numbers.")
                else:
                    result = math.factorial(num)
                    print(f"Factorail of Number {operation} is: ",result)
            except ValueError:
                print("Invalid Input, Please Enter a non negative integer.")

class Percentage(Factorial):
    def percent(self):
        while True:
            operation = input("Choose an operation '%' for calculate Percentage, 'tax' for caluating tax and 'exit' to quit: ")

            if operation.lower() == "%":
                num1 = float(input("Enter value: "))
                num2 = float(input("Total value: "))
                result = (num1/num2) * 100
                print("Percentage: ",result)
            elif operation.lower() == "tax":
                num1 = float(input("Enter tax in percentage: "))
                num2 = float(input("Total value: "))
                result = (num1*num2)/100
                print("Tax or Interest is : ", result)
            elif operation.lower() == "exit":
                break
            else:
                print("Invalid Input, Please enter a non negative integer.")


ob = Percentage()
def Calci():
    while True:
        print("1 -->  CalculateAddSub\n2 --> AdvancedCalculation\n3 -- > LogarithmicOpertions\n4 --> Factorial\n5 --> Percentage")
        operation = input("Choose Operatins for Calculations or exit to quit: ")
        if operation == "1":
            ob.calcu()
        elif operation == "2":
            ob.Adcalcu()
        elif operation == "3":
            ob.loga()
        elif operation == "4":
            ob.Fact()
        elif operation == "5":
            ob.percent()
        elif operation.lower() == "exit":
            break
        else:
            print("Invalid Input, Please Try Again!")
Calci()
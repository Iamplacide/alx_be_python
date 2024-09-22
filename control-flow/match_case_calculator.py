# A program that makes the calculation 

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

match opearation :
    case '+':
        print(num1 + num2)
    case '-':
        print(num1 - num2)
    case '*':
        print(num1 * num2)
    case '/':
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            print(num1 / num2)
    case _: 
        print("Invalid operation.")

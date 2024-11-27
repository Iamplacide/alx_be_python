def perform_operation(num1, num2, operation):
try :
    operand = operation.lower()
    match operand:
        case "add":
            return = num1 + num2
        case "multiply":
            return = num1 * num2
        case "divide":
            return = num1 / num2
        case "subtract":
            return = num1 - num2

except ZeroDivisionError:
    print("Can't divide by zero")

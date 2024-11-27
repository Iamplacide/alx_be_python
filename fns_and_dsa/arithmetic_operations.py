def perform_operation(num1, num2, operation):
    operand = operation.lower()
    match operand:
        case "add":
            return = num1 + num2
        case "multiply":
            return = num1 * num2
        case "divide":
            if num1 == 0 or num2 == 0:
                print("Error! Can't divide by 0)
            else:
                return = num1 / num2
        case "subtract":
            return = num1 - num2

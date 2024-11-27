def perform_operation ():
    print("Arithmetic Operations")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, divide): ").lower()
    
    match operation:
        case "add":
            result = num1 + num2
        case "multiply":
            result = num1 * num2
        case "divide":
            result = num1 / num2
            
    print(f"Result: {result}")



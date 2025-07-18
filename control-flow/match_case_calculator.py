num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ").strip()

match operation:
    case "+":
        print(f"The result of {num1} + {num2} is {num1 + num2}.")
    case "-":
            print(f"The result of {num1} - {num2} is {num1 - num2}.")
    case "*":
        print(f"The result of {num1} * {num2} is {num1 * num2}.")
    case "/":
        if num2 == 0:
            print(f"Cannot divide by zero.")
        else:
            print(f"The result of {num1} / {num2} is {num1 / num2}.")
    case _:
        print(f"Invalid operation '{operation}'. Please use +, -, *, or /.")
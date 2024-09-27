def calculator():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator = input("Enter the operator (+, -, *, /): ")

    if operator == '+':
        result = num1 + num2
        print(f"The sum of {num1} and {num2} is: {result}")
    elif operator == '-':
        result = num1 - num2
        print(f"The subtraction of {num1} and {num2} is: {result}")
    elif operator == '*':
        result = num1 * num2
        print(f"The multiplication of {num1} and {num2} is: {result}")
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
            print(f"The division of {num1} and {num2} is: {result}")
        else:
            print("Error: Division by 0 is not allowed.")
    else:
        print("Invalid operator! we have only four op: +, -, *, /")

if __name__ == "__main__":
    calculator()

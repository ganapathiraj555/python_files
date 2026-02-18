import operator

def calculator():
    try:
        operations = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}

        num1 = float(input("Enter first number: "))
        op = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        result = operations[op](num1, num2)

        print("Result:", result)

    except ValueError:
        print("Error: Please enter valid numbers.")
    except KeyError:
        print("Error: Invalid operator selected.")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
calculator()

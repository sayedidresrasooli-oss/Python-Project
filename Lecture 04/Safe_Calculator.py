class InvalidOperationError(Exception):
    pass

while True:
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        op = input("Enter operation (+, -, *, /): ")

        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            result = num1 / num2
        else:
            raise InvalidOperationError("Invalid operator")

        print("Result:", result)

    except ValueError:
        print("Please enter valid numbers!")

    except ZeroDivisionError as e:
        print(e)

    except InvalidOperationError as e:
        print(e)

    finally:
        print("Calculation attempt completed.")

    choice = input("Try again? (yes/no): ")
    if choice.lower() != "yes":
        break
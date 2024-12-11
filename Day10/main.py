import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(art.logo)
    first_number = float(input("What's the first number? "))

    continue_calculating = True

    while continue_calculating:
        for symbol in operations:
            print(symbol)
        math_operator = input("Pick an operation: ")
        second_number = float(input("What's the next number? "))
        answer = operations[math_operator](first_number, second_number)
        print(f"{first_number} {math_operator} {second_number} = {answer}")

        should_continue = input(f"Type 'y' to continue calculating with {answer} or 'n' "
                                    "to start a new calculation: ").lower().strip()

        if should_continue == "y":
            first_number = answer
            continue_calculating = True
        else:
            continue_calculating = False
            print("\n" * 20)
            calculator()

calculator()
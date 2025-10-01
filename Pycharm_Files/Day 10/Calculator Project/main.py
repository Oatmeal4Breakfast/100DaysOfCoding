from art import logo

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1,n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# Printing the imported logo
print(logo)

first_num = int(input("Enter in the first number: "))
while True:
    for operation in operations:
        print(operation)
    operation  = input("Select the operation you would like to perform: (+, -, *, /)")
    second_num = int(input("Enter in the second number: "))
    result = operations[operation](first_num, second_num)
    print(f"{first_num} {operation} {second_num} = {result}")

    another_operation = input("Would you like to continue working with the previous result? (y/n): ")
    if another_operation.lower() == 'y':
        first_num = result
    else:
        first_num = int(input("Enter in the first number: "))

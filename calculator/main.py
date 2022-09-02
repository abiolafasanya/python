def add(x, y):
    answer = x + y
    print (str(x) + " + " + str(y) + " = " + str(answer))

def sub(x, y):
    answer = x - y
    print (str(x) + " - " + str(y) + " = " + str(answer))

def mul(x, y):
    answer = x * y
    print (str(x) + " * " + str(y) + " = " + str(answer))

def div(x, y):
    answer = x / y
    print (str(x) + " / " + str(y) + " = " + str(answer))

while True:
    print("Welcome to the calculator program!")
    print("Options:")
    print("Enter 'a' to add two numbers")
    print("Enter 'b' to subtract two numbers")
    print("Enter 'c' to multiply two numbers")
    print("Enter 'd' to divide two numbers")

    choice = input("Enter your choice: ")

    if choice == 'a' or choice == 'A':
        x = int(input("Enter the first number: "))
        y = int(input("Enter the second number: "))
        add(x, y)

    elif choice == 'b' or choice == 'B':
        x = int(input("Enter the first number: "))
        y = int(input("Enter the second number: "))
        sub(x, y)

    elif choice == 'c' or choice == 'C':
        x = int(input("Enter the first number: "))
        y = int(input("Enter the second number: "))
        mul(x, y)

    elif choice == 'd' or choice == 'D':
        x = int(input("Enter the first number: "))
        y = int(input("Enter the second number: "))
        div(x, y)

    else:
        print("Invalid input")
        print('Exiting...')
        exit()
        
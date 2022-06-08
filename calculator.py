# Pyhton program to make a simple calculator using functions

# Function definitions for simple calculations
def add(x, y):
    return(x + y)

def subtract(x, y):
    return(x - y)

def multiply(x, y):
    return(x * y)

def divide(x, y):
    return(x / y)

# Capture and evaluate user input
no1 = eval(input("Enter the first number: "))
no2 = eval(input("Enter the second number: "))

# Give user operator options
print("Select an operation")
print("1 = Addition")
print("2 = Subtraction")
print("3 = Multiplication")
print("4 = Division")
print("5 = Exit")

# Capture and return evaluated result based on user's input
# While condition is true
while(True):
    # Caputure user's choice, make sure its a number
    choice = int(input("Which operator did you choose? (Type number): "))

    # Switch statement to evaluate user's numbers based on chosen operator
    def number_chosen(choice):
        match choice:
            case 1:
                print(f"{no1} + {no2} = {add(no1, no2)}")
            case 2:
                print(f"{no1} - {no2} = {subtract(no1, no2)}")
            case 3:
                print(f"{no1} x {no2} = {multiply(no1, no2)}")
            case 4:
                print(f"{no1} / {no2} = {divide(no1, no2)}")
            case 5:
                print(f"Peace!")
                exit()
            case _:
                print(f"Did you select an operation?")

    number_chosen(choice)

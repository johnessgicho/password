import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def power(x, y):
    return x ** y

def sqrt(x):
    return math.sqrt(x)

def sin(x):
    return math.sin(x)

def cos(x):
    return math.cos(x)

def tan(x):
    return math.tan(x)

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Power")
print("6.Square Root")
print("7.Sine")
print("8.Cosine")
print("9.Tangent")

while True:
    choice = input("Enter choice (1/2/3/4/5/6/7/8/9): ")

    if choice in ('1', '2', '3', '4', '5'):
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))

        if choice == '1':
            print(x, "+", y, "=", add(x, y))

        elif choice == '2':
            print(x, "-", y, "=", subtract(x, y))

        elif choice == '3':
            print(x, "*", y, "=", multiply(x, y))

        elif choice == '4':
            print(x, "/", y, "=", divide(x, y))

        elif choice == '5':
            print(x, "^", y, "=", power(x, y))

    elif choice in ('6', '7', '8', '9'):
        x = float(input("Enter a number: "))

        if choice == '6':
            print("√", x, "=", sqrt(x))

        elif choice == '7':
            print("sin(", x, ")=", sin(x))

        elif choice == '8':
            print("cos(", x, ")=", cos(x))

        elif choice == '9':
            print("tan(", x, ")=", tan(x))
    else:
        print("Invalid Input")

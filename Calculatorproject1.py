import math


def add (x,y):
    return x + y
def subtract (x,y):
    return x - y
def multiply (x,y):
    return x * y
def divide (x,y):
    return x / y
def power (x,y):
    return x ** y
def sqrt (x,y):
    return x ** (1 / y)
def factorial(x):
    if x < 0:
        return "Error! Negative Number."
    return math.factorial(int(x))
def mod(x,y):
    return x % y
def sin(x):
    return math.sin(math.radians(x))
def cos(x):
    return math.cos(math.radians(x))
def tan(x):
    return math.tan(math.radians(x))
def radians(x):
    return math.radians(x)
def exp(x):
    return math.exp(x)


print("Select Operation:")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Power(x^y)")
print("6.Square Root")
print("7.Factorial")
print("8.Modulus")
print("9.Sine - Input in Degrees")
print("10.Cosine - Input ")
print("11.Tangent")
print("12.Radians")
print("13.Exponential")
print("0.Exit")

valid = {str(i) for i in range(1, 13)}
single_input = {'6', '7', '8', '9', '10', '11', '12', '13'}

while True:
    choice = input("Select your Operation:3 Hit 0 to close (0-11):").strip()

    if choice == '0':
        print("Goodbye")
        break
    if choice not in valid:
        print("This input is invalid man...try again.")
        continue
    try:
        if choice in single_input:
            if choice == '12':
                x = float(input("Enter Degree of Angle for Radians: "))
                degrees = radians(x)
                radians = degrees * math.pi / 180
                print(f"The Radian is {degrees}")

            elif choice == '13':
                x = float(input("Enter a number (for exponential): "))
            else:
                x = float(input("Enter a number: "))
            x = float(input("Enter a number: "))
            if choice == '6':
                x = float(input("Enter a number to determine the square root: "))
                result = sqrt(x,2)
                print(f"√{x} = {result}")
            elif choice == '7':
                x = float(input("Enter a number to determine the factorial: "))
                print(f"{int(x)}! = {factorial(x)}")
                result = factorial(x)
                print(f"({int(x)}! = {result})")
            elif choice == '9':
                x = float(input("Enter a number to determine the Sine: "))
                result = sin(x)
                print(f"sin({x}°) = {result}")
            elif choice == '10':
                x = float(input("Enter a number to determine the Cosine: "))
                result = cos(x)
                print(f"cos({x}°) = {result}")
            elif choice == '11':
                x = float(input("Enter a number to determine the Tangent: "))
                result = tan(x)
                print(f"tan({x}°) = {result}")

        else:
            a = float(input("Enter the First Number: "))
            b = float(input("Enter a Second Number: "))
            if choice == '1':
                result = add(a,b)
                if result == int(69):
                    print("Nice")
                print(f"({a} + {b} = {result})")
            elif choice == '2':
                result = subtract(a,b)
                print(f"({a} - {b} = {result})")
            elif choice == '3':
                result = multiply(a,b)
                print(f"({a} * {b} = {result})")
            elif choice == '4':
                result = divide(a,b)
                print(f"({a} / {b} = {result})")
            elif choice == '5':
                result = power(a,b)
                print(f"({a} ** {b} = {result})")
            elif choice == '8':
                result = mod(a,b)
                print(f"({a} % {b} = {result})")
            elif choice == '12':
                degrees = float(input("Enter angle in degrees: "))

    except Exception as e:
        print(f"Error: {e}")


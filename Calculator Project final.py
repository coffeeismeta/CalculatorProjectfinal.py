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
def factorial(X):
    if x < 0:
        return "Error! Negative Number."
    return.math.factorial(int(X))
def mod(x,y):
    return x % y
def sin(x)
    return math.sin(math.radians(x))
def cos(x)
    return math.cos(math.radians(x))
def tan(x)
    return math.tan(math.radians(x))

print("Select Operation:")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Power(x^y)")
print("6.Square Root")
print("7.Factorial")
print("8.Modulus")
print("9.Sine")
print("10.Cosine")
print("11.Tangent")
print("0.Exit")

valid = {str(i) for i in range(1, 12)}
single_input = {'6', '7', '8', '9', '10', '11'}

while true:
    choice = input("Select your Operation:3 Hit 0 to close (0-11):").strip()

    if choice == '0':
        print("Goodbye")
        break
    if choice not in valid:
        print("This input is invalid man...try again.")
        continue
    try:
        if choice in single_input:
            x = float(input("Enter a number: "))
            if choice == '6':
                result = root(x,2)
                print(f"√{x} = {result}")
            elif choice == '7':
                print(f"{int(num)}! = {factorial(num)}")
                result = factorial(x)
                print(f"({int(x)}! = {result})")
            elif choice == '9':
                result = sin_deg(x)
                print(f"sin({x}°) = {result}")
            elif choice == '10':
                result = cos_deg(x)
                print(f"cos({x}°) = {result}")
            elif choice == '11':
                result = tan_deg(x)
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
    except Exception as e:
        print(f"Error: {e}")

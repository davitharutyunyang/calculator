import math

operation = input("Input the operation (+, -, *, /, %, ^, //, sqrt, square, pi, e, abs, fabs, sin, cos, tan, arcsin, arccos, arctan, lnx, lgx, e^x, pow, pow10): ").strip().lower()

no_input_needed = operation == "pi" or operation == "e"
single_operand = operation in ("sqrt", "square", "abs", "fabs", "sin", "cos", "tan", "arcsin", "arccos", "arctan", "lnx", "lgx", "e^x", "pow10")

try:
    if not no_input_needed:
        a = int(input("Input the first number:"))
    if not no_input_needed and not single_operand:
        b = int(input("Input the second number:"))
except ValueError:
    print("Error: Input only integers")
    exit()

if operation == "pi":
    print(math.pi)
elif operation == "e":
    print(math.e)
elif operation == "sqrt":
    if a < 0:
        print("Error: Negative number's square root is not possible")
    else:
        print(math.sqrt(a))
elif operation == "square":
    print(a ** 2)
elif operation == "+":
    print(a + b)
elif operation == "-":
    print(a - b)
elif operation == "*":
    print(a * b)
elif operation == "abs":
    print(abs(a))
elif operation == "fabs":
    print(math.fabs(a))
elif operation == "sin":
    print(math.sin(a))
elif operation == "cos":
    print(math.cos(a))
elif operation == "tan":
    print(math.tan(a))
elif operation == "arcsin":
    print(math.asin(a))
elif operation == "arccos":
    print(math.acos(a))
elif operation == "arctan":
    print(math.atan(a))
elif operation == "lnx":
    if a <= 0:
        print("Error: Logarithm of non-positive numbers is not possible")
    else:
        print(math.log(a))
elif operation == "lgx":
    if a <= 0:
        print("Error: Logarithm of non-positive numbers is not possible")
    else:
        print(math.log10(a))
elif operation == "e^x":
    print(math.exp(a))
elif operation == "pow":
    print(math.pow(a, b))
elif operation == "pow10":
    print(math.pow(10, a))
elif operation in ("/", "//", "%"):
    if b == 0:
        print("Error: Division by zero is not possible")
    elif operation == "/":
        print(a / b)
    elif operation == "//":
        print(a // b)
    else:
        print(a % b)
elif operation == "^":
    print(a ** b)
else:
    print("Error: Unknown operation")

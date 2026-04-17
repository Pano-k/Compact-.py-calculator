print("== CALCULATOR ==")
#selection#
selection = input("Type Add, Divide, Subtract, Multiply, or Exponent ")
#number1#
number1 = float(input("== Enter the first number == "))
#number2#
number2 = float(input("== Enter the second number == "))
#result#
if selection == "add":
    print(number1 + number2)
elif selection == "multiply":
    print(number1 * number2)
elif selection == "divide":
    print(number1 / number2)
elif selection == "subtract":
    print(number1 - number2)
elif selection == "exponent":
    print(number1 ** number2)

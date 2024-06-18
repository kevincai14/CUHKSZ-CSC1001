from math import sin
from math import cos
from math import tan

state1 = False
state2 = False
state3 = False

type = ["sin", "cos", "tan"]

while state1 == False:
    functiontype = str(input("Please enter the function type:"))
    judge = functiontype in type
    if judge == False:
        print("Please enter the trigonometric functions!")
        state1 = False
    else:
        state1 = True

while state2 == False:
    try:
        a = float(input("Please enter the interval of star:"))
        b = float(input("Please enter the interval of end:"))
        if a >= b:
            print("Please make sure that a is smaller than b!")
            state2 = False
        else:
            state2 = True
    except:
        print("Please input an integer!")

while state3 == False:
    try:
        n = int(input("Please enter the number of sub-intervals:"))
        state3 = True
    except:
        print("Please input an integer!")

final_result = []

if functiontype == str("sin"):
    for i in range(1, n + 1):
        result = ((b - a) / n) * sin(a + ((b - a) / n) * (i - 1 / 2))
        final_result.append(result)
    print("The result is " + str(sum(final_result)))

elif functiontype == str("cos"):
    for i in range(1, n + 1):
        result = ((b - a) / n) * cos(a + ((b - a) / n) * (i - 1 / 2))
        final_result.append(result)
    print("The result is " + str(sum(final_result)))

elif functiontype == str("tan"):
    for i in range(1, n + 1):
        result = ((b - a) / n) * tan(a + ((b - a) / n) * (i - 1 / 2))
        final_result.append(result)
    print("The result is " + str(sum(final_result)))




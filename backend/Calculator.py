from cmath import sqrt
import math

def calc(eq):
    op = []
    num = []

    i = 0
    j = 0
    while i < len(eq):
        if eq[i] == "+" or eq[i] == "-" or eq[i] == "*" or eq[i] == "/" or eq[i] == "^" or eq[i] == "log" or eq[i] == "exp":
            op.append(eq[i])
        else:
            num.append(eq[i])
            j += 1
        i += 1
    count = 0
    result = 0
    while count < len(op):
        if op[count] == "^":
            ans = float(num[count]) ** float(num[count+1])
            num[count+1] = ans
            del num[count]
            del op[count]
        elif op[count] == "*":
            ans = float(num[count]) * float(num[count+1])
            num[count+1] = ans
            del num[count]
            del op[count]
        elif op[count] == "/":
            ans = float(num[count]) / float(num[count+1])
            num[count+1] = ans
            del num[count]
            del op[count]
        else:
            count += 1
    result += float(num[0])
    for x in range(0, len(op)):
        if op[x] == "+":
            result += float(num[x+1])
        elif op[x] == "-":
            result -= float(num[x+1])
    return result

equation = "2.01^3*2/4"
temp = ""
eq = []
for c in range(0, len(equation)):
    if equation[c] == "+" or equation[c] == "-" or equation[c] == "*" or equation[c] == "/" or equation[c] == "^" or equation[c] == "log" or equation[c] == "exp":
        temp += " "
        temp += equation[c]
        temp += " "
    elif  equation[c] == "(":
        temp += equation[c]
        temp += " "
    elif equation [c] == ")":
        temp += " "
        temp += equation[c]
    else:
        temp += equation[c]
eq = list(temp.split(" "))

i = 0
j = 0
k = 0
bracket = []
result = 0
while i < len(eq):
    if eq[i] == "(":
        j = i + 1
        k = i
        while eq[j] != ")":
            bracket.append(eq[j])
            j += 1
        result = calc(bracket)
        while k <= j:
            del eq[i]
            k += 1
        eq.insert(i, str(result))
    else:
        i += 1
result = calc(eq)
print("%.3f" % result)
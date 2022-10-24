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
            num[count + 1] = ans
            del num[count]
            del op[count]
        elif op[count] == "/":
            ans = float(num[count]) / float(num[count+1])
            num[count + 1] = ans
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
    elif equation[c] == "(":
        temp += equation[c]
        temp += " "
    elif equation[c] == ")":
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


# errorCheck
# Scans the user input String and returns boolean value based on validity of mathematical expression
# Author: Abigail Amethyst
# input - use input String
# Returns true if input is valid mathematical expression, false if otherwise
def errorCheck(s):
    # Remove all spaces if there are any
    s = s.replace(" ", "")
    operators = ['+', '-', '*', '/', '^', 'l', 'e']
    # Returns False if empty string is passed
    if len(s) > 0:
        # Bracket counters for open and closed brackets
        oBrack = 0
        cBrack = 0
        # Scanning through input String
        for i in range(0, len(s)):
            if s[i] == '(':
                oBrack += 1
            if s[i] == ')':
                cBrack += 1
            if s[i] == '.':
                return False
            if s[i] in operators:
                try:
                    # Checking for empty log or exp call
                    if s[i] == 'l' or s[i] == 'e':
                        if s[i + 4] == ')':
                            return False
                    # Checking for double operators
                    elif s[i + 1] in operators[:5]:
                        return False
                except:
                    return False
        # Return False if incorrect bracketing occurs
        if oBrack != cBrack:
            return False
        else:
            return True
    else:
        return False

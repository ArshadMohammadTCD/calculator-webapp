from cmath import sqrt
import math


from flask import Flask, request
import flask
import json
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route("/")
def hello():
    return "Hello, World!"

@app.route('/users', methods=[ "POST"])
def users():
    print("users endpoint reached...")
    # if request.method == "GET":
    #     with open("users.json", "r") as f:
    #         data = json.load(f)
    #         data.append({
    #             "username": "user4",
    #             "pets": ["hamster"]
    #         })
    #         return flask.jsonify(data)
    if request.method == "POST":
        received_data = request.get_json()
        print(f"received data: {received_data}")
        message = received_data['data']
        return_data = calc_api(message)
        return flask.Response(response=json.dumps(return_data), status=201)

if __name__ == "__main__":
    app.run("localhost", 6969)  


def calc(eq):
    op = []      #operator list
    num = []     #number list

    i = 0
    while i < len(eq):
        if eq[i] == "+" or eq[i] == "-" or eq[i] == "*" or eq[i] == "/" or eq[i] == "^" or eq[i] == "log" or eq[i] == "exp":
            if eq[i+1] == "log" and i == 0:                            #check if -log at the start
                neg = math.log10(float(eq[i+2])) * -1
                num.append(neg)
                i += 2
            elif eq[i+1] == "exp" and i == 0:                          #check if -exp at the start
                neg = math.exp(float(eq[i+2])) * -1
                num.append(neg)
                i += 2
            elif eq[i+1] == "-":                                       #check is there neg numbers in the equation
                if eq[i+2] == "log":                                   #check anything like 1 + -log(1) where i should be at "+"
                    neg = math.log10(float(eq[i+3])) * -1
                    num.append(neg)
                    op.append(eq[i])
                    i += 3
                elif eq[i+2] == "exp":
                    neg = math.exp(float(eq[i+3])) * -1                #check anything like 1 + -exp(1) where i should be at "+"
                    num.append(neg)
                    op.append(eq[i])
                    i += 3
                else:
                    neg = float(eq[i+2]) * -1                          #turn to neg numbers and store into the list
                    num.append(neg)
                    op.append(eq[i])
                    i += 2
            elif eq[i] == "-" and i == 0:                              #check is there "-" at the start, e.g.-2+1
                neg = float(eq[i+1]) * -1
                num.append(neg)
                i += 1
            else:
                op.append(eq[i])                                       #if no neg in case, just add to op list
        else:
            num.append(eq[i])                                          #if not operator, then has to be a number(with error checking)
        i += 1

    count = 0
    result = 0

    while count < len(op):
        if op[count] == "^":                                           #"^"should be the first to implement when we have bracket outside
            ans = float(num[count]) ** float(num[count+1])             #calculate answer
            num[count+1] = ans                                         #store into list
            del num[count]                                             #delete the other used number in the list
            del op[count]                                              #delete the used operator
        else:
            count += 1
    
    count = 0                                                          #set count back to 0 to enter another while

    while count < len(op):                                             #check and calculate log and exp before anything else
        if op[count] == "log":
            ans = math.log10(float(num[count]))                        #nature log with a base of 10
            num[count] = ans
            del op[count]
        elif op[count] == "exp":
            ans = math.exp(float(num[count]))                          #calculate exp
            num[count] = ans
            del op[count]
        count += 1
    
    count = 0

    while count < len(op):
        if op[count] == "*":
            ans = float(num[count]) * float(num[count+1])              #calculate mul
            num[count+1] = ans
            del num[count]
            del op[count]
        elif op[count] == "/":
            ans = float(num[count]) / float(num[count+1])              #calculate div
            num[count+1] = ans
            del num[count]
            del op[count]
        else:
            count += 1
    result += float(num[0])                                            #set result to the first value in number list
    for x in range(0, len(op)):                                        #loop through and calculate the rest "+" and "-" operator
        if op[x] == "+":
            result += float(num[x+1])
        elif op[x] == "-":
            result -= float(num[x+1])
    return result                                                      #return final result

def startCalc(equation):
    temp = ""                                                              #temp string to load space
    eq = []                                                                #list of main equation
    index = 0
    while index < len(equation):
        if equation[index] == " ":
            equation = equation.replace(" ", "")
        index += 1

    index = 0
    while index < len(equation):                                           #if operator, add space to front and end, e.g.1+1 turn into 1 + 1
        if equation[index] == "+" or equation[index] == "*" or equation[index] == "/" or equation[index] == "^":
            if equation[index+1] == "-":                                   #if next is also an aperator(negative op), only add space at front
                temp += " "
                temp += equation[index]
            else:                                                          #other operator
                temp += " "
                temp += equation[index]
                temp += " "
        elif equation[index] == "-":                                       #3 cases when "-"
            if index == 0:                                                 #if start with neg element, only add space to the end
                temp += equation[index]
                temp += " "
            elif equation[index+1] == "-":                                 #check anything like 1--1
                temp += " "
                temp += equation[index]
            else:                                                          #normal "-" operator
                temp += " "
                temp += equation[index]
                temp += " "
        elif equation[index] == "l":                                       #in string you get l as the first character
            temp += "log"                                                  #set the whole word log into the list
            temp += " "
            index += 2                                                     #skip character "o" and "g"
        elif equation[index] == "e":                                       #e for exp
            temp += "exp"
            temp += " "
            index += 2
        elif  equation[index] == "(":                                      #open bracket operator
            if equation[index+1] == "-":                                   #check anything like 1+(-1+1)
                temp += equation[index]
            else:                                                          #normal open bracket
                temp += equation[index]
                temp += " "
        elif equation [index] == ")":                                      #close bracket operator
            temp += " "
            temp += equation[index]
        else:                                                              #when is a number
            temp += equation[index]
        index += 1
    eq = list(temp.split(" "))

    i = 0
    j = 0
    k = 0
    t = 0
    s = 0
    l = 0
    bracket = []                                                           #list to calculate bracket
    result = 0
    while i < len(eq):
        if eq[i] == "(":                                                   #if there is a bracket
            j = i + 1                                                      #pointer for the equation in the bracket
            k = i                                                          #temp pointer for i
            while eq[j] != ")":                                            #add equation to the list until find a close bracket
                if eq[j] == "(":
                    bracket.clear()
                    j += 1
                    if t == 0:
                        t += 1
                    s = j - 1
                    l = s
                bracket.append(eq[j])
                j += 1
            result = calc(bracket)                                         #calculate the result
            if t == 0:
                while k <= j:                                                  #check is the temp pointer reach the end of the bracket
                    del eq[i]                                                  #delete the whole bracket
                    k += 1
                eq.insert(i, str(result))                                      #insert the answer into the place of bracket before
                bracket.clear()                                                #clear the bracket for next time
            else:
                while s <= j:                                                  #check is the temp pointer reach the end of the bracket
                    del eq[l]                                                  #delete the whole bracket
                    s += 1
                eq.insert(l, str(result))                                      #insert the answer into the place of bracket before
                bracket.clear() 
                t -= 1
        else:
            i += 1
    result = calc(eq)                                                      #get the whole result
    result = round(result, 3)
    a = str(result)
    i = 0
    while i < len(a):
        if a[i] == ".":
            if len(a) == i+1:
                a += "0"
            elif len(a) == i+2:
                a += "00"
        i += 1
    return a

# errorCheck
# Scans the user input String and returns boolean value based on validity of mathematical expression
# Author: Abigail Amethyst
# s - user input String
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


# calc_api
# Checks user input for valid mathematical expression and returns result based on validity (either result of calculation or error message)
# For use in connecting frontend with backend
# Author: Abigail Amethyst
# s - user input string
# Returns result in string form
def calc_api(s):
    isValid = errorCheck(s)
    if isValid:
        return str(startCalc(s))
    else:
        return "error: invalid input"

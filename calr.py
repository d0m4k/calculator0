#!/usr/bin/python3
#for operator guide
import time
opera = {"1": "plus", "2": "Minus", "3": "multiplication", "4": "division", "5": "Remainder"}
#intro /
print("Welcome from Calculator!!\n\n".center(68))
time.sleep(1)
print("____Guide for calculate____\n")
#/
#Operators uses
opGuide = " '+' for {} \n '-' for {}\n '*' for {} \n '/' for {}\n '%' for {}". format(opera["1"], opera["2"], opera["3"], opera["4"], opera["5"])
print(opGuide)
#Start calculate
def toCal(inp):
    if inp == "+":
        return firstNum + secNum
    elif inp == "-":
        return firstNum - secNum
    elif inp == "*":
        return firstNum * secNum
    elif inp == "/":
        return firstNum / secNum
    elif inp == "%":
        return firstNum % secNum
    else: 
        print ("\n____Check your operator and try Again!!____")
while True:
    firstNum = float(input(" 1st Number: "))
    secNum   = float(input(" 2nd Number: "))
    op = input(" Enter a operator to calculate your value: ")
    data = str(firstNum)+" "+str(op)+" "+str(secNum) + " " + " = "
    result = toCal(op)
    print ("\n\n"+" Your result is "+data+str(result)+"\n\n")

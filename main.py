import math #TUI CALC REMADE
while True:
    num1 = float(input("enter a number "))
    if num1 !="":
        break
while True:
    roka = str(input("enter an operator "))
    if roka !="":
        break
while True:
    num2 = float(input("enter another number "))
    if num2 !="":
        break
def Calc():
    if roka == ("x") or roka == ("*"):
        print (num1*num2)
    elif roka == ('/') or roka == (':'):
        print (num1 / num2)
    elif roka == ("+"):
        print (num1 + num2)
    elif roka == ("-"):
        print (num1 - num2)
    elif roka == ("sqrt"):
        print (math.sqrt(num1))
    elif roka == ("power"):
        print (math.pow(num1, num2))
    return



print (Calc())

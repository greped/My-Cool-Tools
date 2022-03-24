import math

def main():
    print("Calculator for quadratic formula")
    a = eval(input("Insert value a: "))
    b = eval(input("Insert value b: "))
    c = eval(input("Insert value c: "))
    try:
        print("First root is: ", (-b+math.sqrt((b*b)-(4*a*c)))/(2*a))
        print("Second root is: ", (-b-math.sqrt((b*b)-(4*a*c)))/(2*a))
    except:
        print("First root is equal to: ", -b, "-", "sqrt(", ((b*b)-(4*a*c)), ")/", 2*a)
        print("First root is equal to: ", -b, "+", "sqrt(", ((b*b)-(4*a*c)), ")/", 2*a)
main()

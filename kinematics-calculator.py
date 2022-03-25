import math
from PIL import Image
def main():
    print("Find Vf without X, press 1");
    print("Find Vf without time, press 2");
    print("Find Xf without Vf, press 3");
    print("Find Xf without acceleration, press 4");
    print("Find Xf without V0, press 5");
    print("To show equations, press 6");
    while True:
        try:
            x = eval(input("Please enter the number:"))
            if x == 1:
                v0 = eval(input("V0: "))
                a = eval(input("a: "))
                t = eval(input("t: "))
                print("Vf is: ", v0+a*t, "m/s")
            elif x == 2:
                v0 = eval(input("v0: "))
                a = eval(input("a: "))
                xf = eval(input("xf: "))
                x0 = eval(input("x0: "))
                print("vf is: ", math.sqrt((2*a*(xf-x0)+(v0 ** 2))), "m/s")
            elif x == 3:
                x0 = eval(input("x0: "))
                v0 = eval(input("v0: "))
                t = eval(input("t: "))
                a = eval(input("a: "))
                print("xf is: ", x0+(v0*t)+(0.5*a*(t ** 2)), "m")
            elif x == 4:
                x0 = eval(input("x0: "))
                v0 = eval(input("v0: "))
                vf = eval(input("vf: "))
                t = eval(input("t: "))
                print("xf is: ", x0+(0.5*t*(vf+v0)), "m")
            elif x == 5:
                x0 = eval(input("x0: "))
                vf = eval(input("vf: "))
                t = eval(input("t: "))
                a = eval(input("a: "))
                print("xf is: ", x0+(vf*t)-(0.5*a*(t ** 2)))
            elif x == 6:
                # replace the below path with the path to a stored image of the kinematics formula, helps to have)
                imag = Image.open('/home/nosignal/Pictures/kinematicseqs.png')
               imag.show()
            else:
                print("Please enter one of the listed numbers")
            break
        except NameError:
            print("Use a number between 1-5 please")
            continue
main()

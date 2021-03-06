# install Python 3 to your computer. If you use Mac, Windows, or Linux, go here: https://realpython.com/installing-python/
import math
# you need to install pillow, check it out here: https://pillow.readthedocs.io/en/latest/installation.html
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
                # replace the below path ('/home/nosignal...') with the path to a stored image of the kinematics formula, helps to have). If you can't get it to work, just put a # in front of the next two lines.
                imag = Image.open('/home/nosignal/Pictures/kinematicseqs.png')
                imag.show()
            else:
                print("Please enter one of the listed numbers")
            break
        except NameError:
            print("Use a number between 1-5 please")
            continue
main()

# to get this file to work like a calculator, you need to download this file and save it underwhichever name you want as long as the name ends with .py. Use this link to run it: https://techendo.com/post/how-to-run-a-python-script.html

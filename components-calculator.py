# This script can be used to calculate both the x and y (called opposite and adjacent) side lengths and the angle+hypotenuse values.
import math
def main():
    print("Find OPPOSITE and ADJACENT side components, press 1");
    print("Find ANGLE and HYPOTHENUSE side components, press 2");
    answer = input()
    if answer == '1' :
        h = eval(input("Hypotenuse: "))
        O1 = eval(input("Angle: "))
        O2 = math.radians(O1)
        x = h*(math.sin(O2))
        y = h*(math.cos(O2))
        print("Opposite component is: ", format(x, '.4f'), "meters");
        print("Adjacent component is: ", format(y, '.4f'), "meters");
    elif answer == '2' :
        opp = eval(input("Opposite side length: "))
        adj = eval(input("Adjacent side length: "))
        radAng = math.atan((opp/adj))
        degAng = math.degrees(radAng)
        print("Angle is:", format(degAng, '.4f'), "degrees")
        hyp = math.sqrt((opp ** 2)+(adj ** 2))
        print("Hypotenuse is:", format(hyp, '.4f'), "meters")
main()

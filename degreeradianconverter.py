import math
def main():
    print("This script will help you convert radians to degrees or degrees to radians. Please make sure that you follow the instructions below and only\n"
    print("input the value and the word radian or degrees, whichever unit your measurement is in.\n"
    prompt=input("Type the value followed by the word degrees or radians, will solve for other unit: ")
    unit, val = prompt.split(" ")
    if val == 'degrees':
        print(float("{0:0.5}".format(int(unit)*math.pi/180)),"radians")
    elif val == 'radians':
        print(float("{0:0.5}".format(int(unit)*180/math.pi)),"degrees")
main()            

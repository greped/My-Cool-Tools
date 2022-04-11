inInput = input("write numbers here: ").split(",")

happyList = []

for numStr in inInput:
    happyList.append(float(eval(numStr))*0.0254)

print(happyList,"meters")
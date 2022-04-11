#This script converts inches to meters. If you want to use multiple inputs, please space them with a comma and only write the values (i.e. don't add "in." or "inches"
#You do not need to simplify your inputs (i.e. an input of 10+(7/10) will be treated as 10.7)
inInput = input("write numbers here: ").split(",")

happyList = []

for numStr in inInput:
    happyList.append(float(eval(numStr))*0.0254)

print("The following are the values in meters", happyList)

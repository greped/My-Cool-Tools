# hi Dad, hope this script can be of use :)

try:
    totalAmount = float (input("How much was your meal?"));
except ValueError:
    print(f"Please start again and type the dollar value without using the dollar ($) sign, thank you");
try:
    percentage = float (input("what tip percent would like give our staff?"));
except ValueError:
    print(f"Please start again type the percent without using the percent (%) sign, thank you");

tipAmount = (percentage*0.01)*totalAmount;
tipDigits = "{:.2f}".format(tipAmount);
bill = tipAmount+totalAmount;
billDigits = "{:.2f}".format(bill);

print(f"Your tip will be ${tipDigits}, bringing your bill to ${billDigits}.");
print(f"Thank you for your patronage, would you like to hear a complimentary joke? Type yes or no.")

answer = input();

if answer == 'yes' :
    print("Did you know a group of baboons is called a congress? I guess that explains a lot about politics.")
if answer == 'no' :
    print("That's alright, have a nice day!")

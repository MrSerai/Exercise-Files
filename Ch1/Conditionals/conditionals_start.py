# Python for the C# Developer by Joe Marini
# Example code file for conditional statements

# Python only has an if/elif/else construct, unlike C#
# which supports switch statements

x = 10
y = 20
z = 30

num1=15
num2=3
num3=10

# TODO: define an if-elif-else structure
if num1<num2:
    print("first condition executed")

elif num3 >num1 and num2<num3:
    print("second Condition Executed")

else:
    print ("last statement executed")

# TODO: use the compact if-else format
print("5th condition executed") if x>y else print("6th condition executed")
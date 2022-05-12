# Example file for the Python for the C# Developer LinkedIn Learning course by Joe Marini

# TODO: Variables can be declared without an explicit type

car="BMW"
# TODO: re-declaring the variable works
myName="Mr ALlucious"
print(myName)
myName="Mr Beau"
print(myName)



# TODO: ERROR: variables of different types cannot be combined

mNUM=5

print(myName+" " +str(mNUM))

# TODO: Global vs. local variables in functions
def changeName():
    global myName 
    myName="Mr Taki"

    #take note the function declares a new local variable, even though the local and global variables have the same names with the same caps. 
    # when you print or access the variable outside of the function it will return global variable... the local on is limited within the function 

print(changeName())

print(myName)
# TODO: use the del operator to un-declare a variable

del mNUM


#the line below should throw an error because imNUM is undefined
#print(mNUM)

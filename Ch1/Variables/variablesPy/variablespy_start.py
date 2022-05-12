# Example file for the Python for the C# Developer LinkedIn Learning course by Joe Marini

# TODO: Variables can be declared without an explicit type

car="BMW"
# TODO: re-declaring the variable works
my_name="Mr ALlucious"
print(my_name)
my_name="Mr Beau"
print(my_name)



# TODO: ERROR: variables of different types cannot be combined

my_num=5

print(my_name+" " +str(my_num))

# TODO: Global vs. local variables in functions
def changeName():
    global my_name 
    my_name="Mr Taki"

    #take note the function declares a new local variable, even though the local and global variables have the same names with the same caps. 
    # when you print or access the variable outside of the function it will return global variable... the local on is limited within the function 

print(changeName())

print(my_name)
# TODO: use the del operator to un-declare a variable

del my_num


#the line below should throw an error because imNUM is undefined
#print(mNUM)

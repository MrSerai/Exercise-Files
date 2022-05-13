# Exercise file for Python for the C# Developer LinkedIn Learning course by Joe Marini

# functions are defined using the def keyword, then
# the : character and whitespace define the function body
def a_func():
    print("this is a line in my function that returns a value")
    return 10258

def my_returnable_func(a,b):
    print("this is a line in my void function without a return statement")
    print(a+b)


#this function  contains an args paramater that is sort of like an array
def variable_arguments(a,b,*args):
    print(a+b)
    for arg in args:
        print(arg)




#returned_val=a_func()
#instead of assigning the returned value to a variable It just displays directly
print(a_func())

print(my_returnable_func(10,5))


variable_arguments(29,21,50,"sdcasz",789456,"HELLO wORLD")
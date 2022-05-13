# Exercise file for Python for the C# Developer LinkedIn Learning course by Joe Marini

# Python provides a way to require that some arguments can only be called
# by keyword. This is usually used when the argument is important and you
# want the caller to explicitly use the argument name

 
def myFunction(arg1, arg2,*, suppressExceptions=False):
    print(arg1, arg2, suppressExceptions)

def test_func(*,name,surname,age):
    print(name,surname,age)


myFunction(1,4,suppressExceptions=True)



#the * forces the caller of the function to explicitly name the variable
test_func(name="Allucious",surname="Serai",age=15)
# Exercise file for Python for the C# Developer LinkedIn Learning course by Joe Marini

# Functions can have default parameter values like in C#
# They can also be explicitly used in the calling location


# Functions can then be called using named parameters
# once you use a named parameter, all following params must be
# called by name as well


#you can also assign variable defaults in the parameters of the function, this will overide what was sent in the reference.
def named_params_with_defaults(name,age,allow_access=False):
    if allow_access:
        print("age comes first")
        print(age)
        print(name)
    else:
        print("name comes first")
        print(name)
        print(age)
#you can also assign variables  within the function reference
named_params_with_defaults("Allucious",age=18,allow_access=True)
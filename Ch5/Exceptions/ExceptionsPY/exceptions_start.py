# Example file for the Python for the C# Developer LinkedIn Learning course by Joe Marini

# Exceptions in Python are similar to those in C#
# There's a try-except-finally mechansism
from email.mime import nonmultipart


try:
    a=100
    b=52
    c=None
   
    x=int(c)
    if a>10:
        raise ValueError("Can't go higher than 10")
    x=a/b
    print("result is ",x)

   
except ZeroDivisionError as e:
    print("OH NO My Friend ",e)  

except ValueError as e:
    print("uh oh", e)
except BaseException as e:
    print(e)
finally:
    print("this code always runs")
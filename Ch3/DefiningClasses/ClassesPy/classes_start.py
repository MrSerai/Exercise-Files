# Exercise file for Python for the C# Developer LinkedIn Learning course by Joe Marini

# TODO: Classes are defined using the class keyword
from xxlimited import new


class Book:
    def __init__(self,title,author,price) :
        self._title=title
        self._author=author
        self._price=price

    @property
    def price(self):
        return self._price
    @price.setter
    def price(self,value):
        self._price=value
    @property
    def author(self):
        return self._author

    @author.setter
    def author(self,value):#the setter function recieves the __init__ and the user's entered value as a param
        self._author=value#changes the contents of the global private variable with the user entered value
    
    @property
    def title(self):#the function recieves the __init_ method as a param
        return self._title
        #the above can be considered as a getter method

    @title.setter
    def title(self,value):
        self._title=value


# TODO: create an instance of the class
b1=Book("War and Peace","Leo Tolstoy",2586)

print(b1.title)

print(b1.author)

print(b1.price)

b1.price=239
print(b1.price)

b1= Book("THE ART of War and Peace","Sun Tsu",2586)

print(Book)
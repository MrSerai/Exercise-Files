# Exercise file for Python for the C# Developer LinkedIn Learning course by Joe Marini

# Define some data to use in our functions
from unicodedata import name


numbers = [10, 6, 23, 15, 18, 59, 62, 7, 103, 29, 35]
names = ["Amy", "Adam", "Benjamin", "Elise", "Terry", "Ziggy"]
somestr = "The quick brown fox jumped over the lazy dog"

# TODO: The len function will return the length of any iterable
print(len(numbers))
print(len(somestr))


# TODO: min and max calculate the smallest and largest values
smallest_number=min(numbers)
biggest_number=max(numbers)
print(smallest_number,biggest_number)


# TODO: min and max can also use a key function to provide a comparable value
smallest_name=min(names, key=lambda x:len(x))
longest_name=max(names, key=lambda x: len(x))
print(smallest_name,longest_name)


# TODO: The sorted function will return a new sorted list from an iterable
    #sorting numbers from lowest to highest
print(sorted(numbers))


    #sorting alphabets in order
print(sorted(somestr))

   
    #sorting the names according to thier length (shortest to longest)
print(sorted(names,key=lambda x: len(x)))

# TODO: any and all can be used to perform a test on a set of data
    #anny function to check if there are any names that are longer than 5 characters
print(any(len(w) > 5 for w in names))

#find if all the characters of the names are longer than 20 characters in the array
print(all(x>20 for x in numbers))
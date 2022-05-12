
# Example code file for loops

# the Python for loop always acts as an iterator - the typical
# (init value, test, increment) pattern isn't something you see in Python

# TODO: to iterate over a count, you create a numerical iterator with range()

#the line below forLoop is to print a range of numbers within the range of 11. 
#within that loop there is an if statement to make sure that there is no comma printed after the last number returned

for i in range(11):     
    if i==10:
         print(i) 
    else:
        print(i, end=", ")  


print("\n---------")

for i in range(-11,12,2):
    if i==11:
         print(i) 
    else:
        print(i, end=", ") 

          
print("\n---------")

# TODO: iterating over a collection or string is the same as with C# foreach,



# but we use the same "for" keyword
my_characters = "Man this is one long string! i can't believe i choose such a long string... oh when will it end!? the pain! the agony!!! Just Kidding :)"
for chars in my_characters: 
    if chars==")":
        print(chars,end=" ")

    else:
        print(chars,", ",end=" ")
print("\n---------")

# TODO: if you really need an index, you can use enumerate()
for i,c in enumerate(my_characters):
    print(str(i)+", "+c+", ",end=" ")
print("\n---------")


# TODO: Similarly, there's only a while loop in python and no do-while, which
# is just syntactic sugar for a loop that always executes at least once
continue_iterating = True
i = 0
while(continue_iterating):
    print("Number: ",i)
    i+=1

    if i >100:
        continue_iterating=False

# Exercise file for Python for the C# Developer LinkedIn Learning course by Joe Marini

data = [10, 6, 23, 15, 18, 59, 62, 7, 103, 29, 35]

# regular sort
print("Sorted:")
result = sorted(data)
print(result)

# TODO: sort using a lambda
print("Sort by first digit:")


#sorting the data(first param) using the lamda with a x variable assigned .
#from the variable index take the first character and apply the sort using the first character
result=sorted(data,key=lambda x: str(x)[0])
print(result)


#from the variable index take the first character and apply the sort using the Second character

data_array = [150, 66, 203, 175, 128, 59, 62, 78, 103, 279, 345]
sorted_result=sorted(data_array,key=lambda y:str(y))
print(sorted_result)


#from the variable index take the first character and apply the sort using the Second character

print("______________Sort by second Digit_____________________")
sorted_result=sorted(data_array,key=lambda y:str(y)[1])
print(sorted_result)
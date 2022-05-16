# Exercise file for Python for the C# Developer LinkedIn Learning course by Joe Marini

fruitlist = [] #declare empty arry
newlist = [1, False, "bob"]

# TODO: append data to a list
fruitlist.append("Bmw")
fruitlist.extend(["orang","Bananaa"])#extend can be used for adding multiple cells into the array
# TODO: insert data


# TODO: search for a list item

print(fruitlist.index("Bmw"))

print("Bmw" in fruitlist)
# TODO: modify an item in-place
fruitlist[2]="apple" #this only works if the index already exists and has a value
print(fruitlist)
# TODO: remove an item

fruitlist.remove("apple")
print(fruitlist)
# TODO: empty the list


# TODO: lists can be created using the list() global function




print(fruitlist)

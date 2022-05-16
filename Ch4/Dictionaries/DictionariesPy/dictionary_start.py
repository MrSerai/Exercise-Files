# Exercise file for Python for the C# Developer LinkedIn Learning course by Joe Marini

# declare an empty dictionary



from cupshelpers import Printer


fileDesc = {}
# dictionaries can also be declared with initial content
nums = {1: "one", 2: "two", 3: "three"}

# TODO: add some items
fileDesc["pdf"]="Protable Document Format"
fileDesc["txt"]="Text File"
fileDesc["rtf"]="Rich Text Format"
fileDesc["jpg"]="JPEG Image"
fileDesc["png"]="Portable Network Graphic Image"
print(fileDesc)
# TODO: get the item count

print("----------------------------------------")
print(f"Dictionary contains {len(fileDesc)} items")
# TODO: adding an existing key just replaces the item
fileDesc["SGabana"]="SGB zwino"
print(fileDesc["SGabana"])



fileDesc["SGabana"]="SGB zwino 2"
print(fileDesc["SGabana"])

# TODO: check if a key exists
print(fileDesc.keys())


print("++++++++++++++++++++++++++++++++=")
print("txt" in fileDesc.keys())

# TODO: check if a value exists

print("Text File" in fileDesc.values())
# TODO: remove a single item

del fileDesc["SGabana"]
print(fileDesc)


print("----------------------")
print ("SGabana" in fileDesc.keys())
# TODO: clear all values
print(f"Dictionary contains {len(fileDesc)} items")
fileDesc.clear()
print(f"Dictionary contains {len(fileDesc)} items")
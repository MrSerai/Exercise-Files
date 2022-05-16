# Example HelloWorld file for the Python for the C# Developer LinkedIn Learning course

thestr = "The quick brown fox jumps over the lazy dog"
alpha1 = "abcdef"
alpha2 = 'ABCDEF'

# TODO: getting the string length
print(len(thestr))

# TODO: working with substrings
print(thestr)
print(thestr.startswith("The"))
print(thestr.endswith("dog"))

print(thestr.find("fox"))

#substring ,getting 
print(thestr[4:9])


#the replacing fox with cat  
newstr  =thestr.replace("fox","cat")

print(newstr)
# TODO: string concatenation
strlist=[]
for i in range(10):
    strlist.append(str(i))
thestr="".join(strlist)
print(thestr)

thestr="".join("my")
thestr="".join("name")
thestr="".join("is")
thestr="".join("Jeff")

print(thestr)
# TODO: string interpolation
  
interp=f"Lower case letters are {alpha1}, Upppercase are {alpha2}"

print(interp)
interp2=f"{len(alpha1)}"
print(interp2)
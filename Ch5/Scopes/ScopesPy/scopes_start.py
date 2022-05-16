# Exercise file for Python for the C# Developer LinkedIn Learning course by Joe Marini

# TODO: Python uses the "with" statement to define a scope block



with open("MyTextFile.txt","r") as thefile:
    linecount=0
    while True:
        thestr=thefile.readline()
        if not thestr:
            break
        print(thestr)
        linecount+=1
    print(f"The file has {linecount} lines")

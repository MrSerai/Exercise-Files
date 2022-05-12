from ast import Pass


tswellaPele=True
tallyNumber=0
userInput=""

print("Enter a number to start the tally,Enter 'quit' to stop")

while(tswellaPele):
    try: #got try from the solution  O_O
        userInput=input()
        if userInput=="quit":
            tswellaPele=False
        else:
            tallyNumber+=int(userInput)
            print(tallyNumber)
    except ValueError:
        Pass
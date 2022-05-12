from ast import Pass


tswella_pele=True
tally_number=0
user_input=""

print("Enter a number to start the tally,Enter 'quit' to stop")

while(tswella_pele):
    try: #got try from the solution  O_O
        user_input=input()
        if user_input=="quit":
            tswella_pele=False
        else:
            tally_number+=int(user_input)
            print(tally_number)
    except ValueError:
        Pass
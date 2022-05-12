# Example HelloWorld file for the Python for the C# Developer LinkedIn Learning course

import datetime


#function to calculate the user's birth year
def calcBirthYear(age):
    currentDate= datetime.date.today()
    birthyear=currentDate.year-age
    return birthyear
    



#function to get all User inputs and display final output after calculating the birth year
def In_out():
    myName = input("Enter Name: ")
    Surname = input("Enter your Surname: ")
    age = int (input("Enter Your Age: "))
    bYear=calcBirthYear(age)
    
    #Displaying Final Output
    print(f"Hello {myName + ' ' + Surname} it Is a pleasure to meet you, and you Are {age} years Old. you were born in the year {bYear}")
     ##print(f"Hello {myName + ' ' + Surname} it Is a pleasure to meet you, and you Are {age} years Old.")

#if the file is being run as a main program the if statement will execute
if __name__=="__main__":
    In_out()



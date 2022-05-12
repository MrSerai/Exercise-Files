# Example HelloWorld file for the Python for the C# Developer LinkedIn Learning course

import datetime


#function to calculate the user's birth year
def calc_birth_year(age):
    current_date= datetime.date.today()
    birthyear=current_date.year-age
    return birthyear
    



#function to get all User inputs and display final output after calculating the birth year
def in_out():
    my_name = input("Enter Name: ")
    surname = input("Enter your Surname: ")
    age = int (input("Enter Your Age: "))
    b_year=calc_birth_year(age)
    
    #Displaying Final Output
    print(f"Hello {my_name + ' ' + surname} it Is a pleasure to meet you, and you Are {age} years Old. you were born in the year {b_year}")
     ##print(f"Hello {myName + ' ' + Surname} it Is a pleasure to meet you, and you Are {age} years Old.")

#if the file is being run as a main program the if statement will execute
if __name__=="__main__":
    in_out()



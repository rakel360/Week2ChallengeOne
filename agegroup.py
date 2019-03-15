
from datetime import datetime

def myAgeGroup():
    #gets current year from system
    current_year= datetime.now().year

    #prompts user to enter year of birth
    birth_year= int(input("Enter your birth year: "))
    
    if birth_year<0 or birth_year>current_year:
        print('Please enter valid year')
    else:
        age= current_year-birth_year
        print("You are " + str(age) + "years old")
        if age<18:
            print("You are a minor")
        elif age>=18 and age<=36:
            print("You are a youth")
        else:
            print("You are an elder")

myAgeGroup()
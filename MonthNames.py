# Exercise 1 
# Name your file: MonthNames.py 
# Write a program that reads an integer value between 1 and 12 from the user and prints output the corresponding month of the year.
# An example run of the program (numbers in bold are typed in by the user) Enter the month: 3 Month 3 is March 

number = int(input("Enter an integer value between 1 and 12: "))
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
if(number >= 1 and number <=12):
    print(f"Month {number} is {months[number-1]}")
else:
    print("Invalid input")



# Output :
# Enter an integer value between 1 and 12:  6
# Month 6 is June
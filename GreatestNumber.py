# Exercise 4 
# Write a Python program to receive 3 numbers from the user and print the greatest among them. 
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
if (num1 > num2 and num1 > num3):
    print("Greatest number = ", num1)
elif (num2 > num1 and num2 > num3):
    print("Greatest number = ",num2)
else:
    print("Greatest number = ",num3)



# Output :
# Enter the first number:  5
# Enter the second number:  25
# Enter the third number:  30
# Greatest number =  30
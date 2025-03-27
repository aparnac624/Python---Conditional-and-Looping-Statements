# Exercise 5 
# Find the factorial of a given number using loops ( note the number is received from the user) 

number = int(input("Enter a number :"))
fact = 1
for i in range(1,number+1):
    fact = fact*i
print("Factorial of the number =",fact)


# Output :
# Enter a number : 5
# Factorial of the number = 120
# Exercise 6 
# Reverse a number using while loop 

num = int(input("Enter a three-digit number :"))      
reversed_no = 0
while (num > 0): 
    reversed_no = reversed_no * 10 + num % 10         
    num = num//10   
    
print("Reversed number :", reversed_no)


# Output:
# Enter a three-digit number : 351
# Reversed number : 153
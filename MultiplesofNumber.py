# Exercise 7 
# Finding the multiples of a number using loop

number = int(input("Enter a number :"))
limit = int(input("Enter the limit :"))
print(f"Multiples of {number} upto {limit} :", end=" ")
for i in range(1,limit+1):
    if(i%number == 0):
        print(i,end=" ")



# Output :
# Enter a number : 5
# Enter the limit : 25
# Multiples of 5 upto 25 : 5 10 15 20 25 
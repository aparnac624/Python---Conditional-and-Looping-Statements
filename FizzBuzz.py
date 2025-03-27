# Exercise 9 
# Write a program that prints the numbers from 1 to 10. But for multiples of three print "Fizz" instead of the number and for the multiple of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz" 

for i in range(1,11):
    if(i%3 == 0 and i%5 == 0):
        print("FizzBuzz")
    elif(i%3 == 0):
        print("Fizz")
    elif(i%5 == 0):
        print("Buzz")
    else:
        print(i)



# Output :
# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
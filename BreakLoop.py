# Exercise 8 
# Write a program to print the inputted value as it is and break the loop if the value is 'done'. 
# Example run of the program :hello there hello there :finished finished :done Done 

while True:
    user_input = input("Enter a value: ")
    if user_input == 'done':
        print("Done")
        break
    print(user_input)



# Output :
# Enter a value:  anupama
# anupama
# Enter a value:  anu
# anu
# Enter a value:  saw
# saw
# Enter a value:  done
# Done
# Write a Python program that does the following:
    # Creates an empty list called my_list.
    # Prompts the user to enter 5 integers, one at a time, and appends them to my_list.
    # Prints the sum of all the integers in my_list to the user.
    # Prints the largest and smallest integers in my_list to the user using the max() and min() functions, respectively.

# Create an empty list called my_list
my_list = []

# Inform the user what's expected
print("Please enter 5 integers:")

# Loop 5 times to get user input and append to the list
for i in range(5):
    # Prompt the user to enter an integer
    number = int(input(f"Enter integer {i+1}: "))
    my_list.append(number)

total = sum(my_list)
largest = max(my_list)
smallest = min(my_list)

print("The Sum Of all Integers is,", total)
print("The largest integer is:", largest)
print("The smallest integer is:", smallest)
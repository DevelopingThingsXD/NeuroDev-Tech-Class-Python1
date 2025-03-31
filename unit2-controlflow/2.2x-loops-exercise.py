# Write a program that handles the "FizzBuzz" problem.
# The program will print every number from 1 to 100, with some exceptions:
# If the number is divisible by 3, print "Fizz" instead of the number.
# If the number is divisible by 5, print "Buzz" instead of the number.
# If the number is divisible by both 3 AND 5, print "FizzBuzz".

# The output should look like this:

'''
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
etc...
'''
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)


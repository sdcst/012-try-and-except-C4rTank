#!python3

# Reciprocal
# have the user enter numbers and determine the 
# reciprocal of each number as a decimal and print it.
# use the try/except to find any invalid values and display
# the error message

#sample output:
"""
Enter a number: 0
The reciprocal of 0 does not exist
Enter a number: 1
The reciprocal of 1 is 1.0
Enter a number: 2
The reciprocal of 2 is 0.5
Enter a number: 3
The reciprocal of 3 is 0.3333333333333333
Enter a number: 4
The reciprocal of 4 is 0.25
"""

num = input("Please enter in a value :")

try: 
    num_i = int(num)
    num_f = 1 / num_i
    num_f = float(num_f)
    print("The reciprocal of",num_i,"is",num_f)
except Exception as e:
    print("The reciprocal of",num_i,"does not exist")

#done

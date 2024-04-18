#!python3

# Retrieve numerical input

# The following code will not work if the user enters in 
# invalid characters (ie non numerical characters)
# modify this code with  a try...except 
# block so that the user will allow them to enter an integer,
# or display an error message if they enter in something else.

number = input("Please enter in an integer value :")
number = number

try: 
    number = int(number)
    print("The number you entered is",number)
except Exception as e:
    print(number,"is an invalid character!")

#done


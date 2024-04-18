#!python 3

# Square root of a number

# Have the user enter in a number.  Use a try-except to see if the input
# is a valid number.  Determine the square root and use a try-except to
# catch exceptions if the number can not be square rooted
# note: Use the math.sqrt() function to determine a square root
# rather than number**(0.5) as we need to catch complex numbers as
# exceptions

"""
Sample Output
Enter a number:x
That is not a valid number
There is no square root   
Enter a number:-1
There is no square root
Enter a number:3       
The square root of 3.0 is 1.7320508075688772
"""
import math

num = input("Please enter in a value :")
try: 
    num = float(num)
    new_num = math.sqrt(num)
    print("The square root of",num,"is",new_num)
    
except Exception as e:
    try: 
        num == num + 1 == int or float
        print("There is NO square root!")
    except:
        print(num,"is not a valid number")
        print("There is NO square root!")

#done



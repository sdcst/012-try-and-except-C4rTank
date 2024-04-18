#python3
# Quadratic Equation
# Have the user enter in the coefficients of a quadratic equation in the
# format: ax^2 + bx + c = 0 and calculate the solutions of the equation
# rounded to 2 decimal places. Use a try...except block to catch if there
# is no solution


""" Sample output:
Enter in the coefficients for a quadratic equation in the format:
  ax^2 + bx + c = 0
a:3
b:d
c:1
Those are not valid values for a, b or c
a:3
b:2
c:1
There are no real roots to the equation
a:2
b:-3
c:-6
The roots are 2.64 and -1.14
a:1
b:8
c:16
The roots are -4.0 and -4.0
"""
import os
import math
os.system('cls')


print("Enter in the coefficients for a quadratic equation in the format: ")
print("ax^2 + bx + c = 0")
a = input ("Enter value for a :")
b = input ("Enter value for b :")
c = input ("Enter value for c :")


try:
  a = int(a)
  b = int(b)
  c = int(c)
  st1 = b**2 - 4 * a * c
  st2 = math.sqrt(st1)
  st3a = -1 * b + st2
  st3b = -1 * b - st2
  st4a = st3a / 2 * a
  st4b = st3b / 2 * a
  st4a = round(st4a,2)
  st4b = round(st4b,2)
  print("The roots are",st4a,"and",st4b)

except Exception as e:
    
    try:
      a / a and b / b and c / c == 0
      print("There are no real roots to the equation")
    except:
      print("Those are not valid values for a, b or c")

#done


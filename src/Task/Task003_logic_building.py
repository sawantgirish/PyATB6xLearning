'''
write a program to calsulate the are of circle
given its radius using formula  area= pi * r**2 where pi=3.14
'''

# Input = float
# output = string
#logic building formula
#  step 1 -> fihure out what is the Input and the output
# input -> r-> datatype->flaot
#pi= 3.14
#power -> pow or ** -> any
# output ->string-> float- area,print area
#  0Step 2 -> rough Logic -> area = 3.14* pow(r,2)
# Step 3
radius = float(input("enter the radius of circle\n"))
print(radius)
#area = 3.14 * (radius**2)
area = 3.14 * pow(radius,2)
print("Area of the circle is ", area)

#String  Data Formating
print(f"The area of the circle is {area:2f}", area)
'''
here f is used ofr data formating and the curly bracted where 2f is metioned is
 for to make sure we can get the decimal in .00  format (that is . 2 decimal format)
  , we can change the number based on our choice))
  it can be used for only  float datatype
'''
# Write a Python program to calculate the
# area of a circle given its radius using the formula
# ``` area=π×r^2``` ( Take pie as 3.14)
import math

# i/p - r - float
# o/p  -> string formatted output of area.


# Logic Building Formula
# || Step 1 ||
# Figure out the inputs and output
# input -> r ->  data type -> float
# pi = 3.14
# power -> pow or ** -> any
# o/p -> String -> float - area , print area

# || Step 2 ||
# rough logic =  area = 3.14 * pow(r,2)


# || Step 3 ||
radius = float(input("Enter the radius of the circle\n"))
print(radius)
# area = 3.14987654 * (radius**2)
area = math.pi * pow(radius,2)

print("Area of the circle is -> ", area)

# String data formatting , Python f-strings, formatted string literals
print(f"Area of the circle is -> {area:.2f}")
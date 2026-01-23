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

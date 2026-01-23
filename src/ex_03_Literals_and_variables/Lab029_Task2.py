# take user input of two number
# print Quotient and Reminder
'''
eg-> num1= 15, num2= 2
here when 15 is divided by 2 we get
7 as a Quotient and 1 as a reminder
'''
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))

quotient=num1//num2 # when we use / twice then we can get Quotient
reminder=num1%num2

print(quotient)
print(reminder)
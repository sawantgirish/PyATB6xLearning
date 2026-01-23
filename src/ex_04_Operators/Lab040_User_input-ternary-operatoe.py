user_age = int(input("my age is \n"))

if user_age >= 18:
    print("you are a allowed to vote")
else:
    print("you are not allowed to vote")

print("you are a allowed to vote" if user_age >= 18 else "you are not allowed to vote" )
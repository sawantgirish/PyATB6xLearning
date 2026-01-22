name = "This  is my name"
print(type(name))
# name = name + 1 (we cannot do this as concatation is not allowed )
# instead we can convert it into str and the use it
name = name + str(1)
print(type(name))

first_name = "Girish"
last_name = "Sawant"
full_name = first_name + " " + last_name
print(full_name)
print(type(full_name))
# Using % operator
name = "Mohan"
age = 19
result = "My name is %s and I am %d years old." % (name, age)
print(result)  # "My name is Mohan and I am 19 years old."

# Using str.format() method
result = "My name is {} and I am {} years old.".format(name, age)
print(result)  # "My name is Mohan and I am 19 years old."

# Using formatted string literals (f-strings)
result = f"My name is {name} and I am {age} years old."
print(result)  # "My name is Mohan and I am 19 years old."
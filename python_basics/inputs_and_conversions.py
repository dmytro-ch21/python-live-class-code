# print("This is input section.......")

# # Lets prompt for an input
# first_name, last_name = input("Enter your full name: ").split() # separates the values by spaces by default
# print(f"Nice to meet you: {first_name} {last_name}")

# firsta_name, last_name, age = input("Enter your Full name and age space separated: ").split()
# print(firsta_name, type(firsta_name))
# print(last_name, type(last_name))
# print(age, type(age))

# the issue is that we have all values as str.
# what is we need to do some math? 

# conversions - type casting

# convert to int()
# age = input("What is your age: ")
# print(age, type(age).__name__)
# age = int(age)
# print(age, type(age).__name__)
# print(age + 10) # 20 + 10 = 30, 20 + 10 = 2010

# print("Taking input completed!")



# Integer Casting

# result = int(5.99999) # float
# result = int("42") # str
# result = int(True) # bool
# result = int(False) # bool
# result = int("False") # str as bool - error
# print(result, f"-- Type is: {type(result).__name__}")
# print(True + 100) # True (Object) -> 1 or 0

# # Float Casting - Conversions
# output = float(5) # int to float
# output = float("3.89") # int to float
# output = float(True) # int to float
# print(output, f"-- Type is: {type(output).__name__}")

# # String conversions
# age = str(25)
# output = str(3.14)
# output = str(True)
# output = str([1, 2, 3])
# print(output, f"-- Type is: {type(output).__name__}")


# Boolean conversions
# falsy: 0, ""/''/""""""/'''''', {}, [], False
print(bool(0))
print(bool(""))
print(bool(''))
print(bool(""""""))
print(bool([]))
print(bool(False))

print(bool(-10))
print(bool([False]))
print(bool("""."""))
print(bool(" "))
print(bool("False"))

# string to list
text = "Hello, Bob!"
print(list(text))
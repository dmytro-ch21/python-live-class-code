# declare and assign
age = 50
age = "Fifty"
age = True

# Type notations are just hints, they don'tr enforse this by default
# To make work we will need to insatll additional static checker (e.g. guardtyping)
name: str = "Bob"
name = 120

print(age, type(age))
print(name, type(name))

# multiple assignment same value
x = y = z = 100
print(x, y, z)
# multiple assignment different values
a, b, c = "Hello", "World", 2025
print(a, b, c)

# swapping values with multiple assignment 
num1 = 100
num2 = 200
print(f"num1 = {num1}, num2 = {num2}")

# make the logic that swaps the values
num1, num2 = num2, num1
print(f"num1 = {num1}, num2 = {num2}")

# declare with no value
full_name = None
# reassign later
full_name = "Bob Dylan"
print(full_name)




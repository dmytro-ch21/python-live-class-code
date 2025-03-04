# Arithmetic Operators
a, b = 10, 3
# +
print(a + b)
# -
print(a - b)
# /
print(a / b)
# //
print(a // b)
# *
print(a * b)
# %
print(a % b) # 10 % 3 = 10 - (9) = 1 
# **
print(a ** b)

# precedence - pemdas
print((10 - 2) * 2)

# division by 0
# print(a / 0)

# negative floor division
print(-10 // 3) # -3.33333333333 -> -4

# negative modulus
print(-10 % 3) 
# -10 % 3 = -10 - (3 * (-10 // 3))
# -10 % 3 = -10 - (3 * (-4))
# -10 % 3 = -10 - (-12)
# -10 % 3 = -10 + 12
# -10 % 3 = 2

# concatenation
first = "Alice"
last = "Doe"
full_name = first + " " + last

# print("1010" + 10)

# repetition of strings 
print("Hello " * 10)
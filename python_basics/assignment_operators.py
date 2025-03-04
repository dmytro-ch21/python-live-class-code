# Assignment Operators
# count = 10
# # print(count)

# # add to the existing value
# # count = count + 10
# # print(count)
# # count += 20
# # print(count)

# # subtraction
# # count = count - 4
# # print(count)
# # count -= 6
# # print(count)

# count /= 2
# print(count)
# count *= 10
# print(count)
# count //= 3
# print(count)
# count **= 2
# print(count)
# count %= 3
# print(count)

# # There no increment and decrement ++ and --
# x = 0
# x += 1
# x += 1
# x += 1
# x -= 1
# print(x)

# Unary Operators

# # unary (-) negate
# num = -10
# print(-num)

# # unary (+) keep same value
# count = -60
# print(+count)

# # bitwise not(~)
# x = 5
# print(~x) #-(x + 1)

# num = 10
# print(bin(num))

# Comparison Operators
# a = 10
# b = 20

# print(a == b)
# print(a != b)
# print(a > b)
# print(a < b)
# print(a >= b)
# print(a <= b)

# age = 20

# # if huest is more than 16 and should less than 40
# print(age > 16 and age < 40)
# # python allow you to use multiple inline comparison with one operator
# print(16 < age < 40)

# # cat vs car

# print("cat" > "car")
# is first letter same -> c vs c
# is second letter same -> a vs a
# t > r -> t(116) > r(114)

# print("apple" > "banana")
# print("Hi" > "Hello")
# # i(105) > e(101)
# print("Apple" > "apple")


# # Logical Operators
# print(True and True)
# print(True and False)
# print(False and True)
# print(False and False)
# print("-" * 10)
# print(True or True)
# print(True or False)
# print(False or True)
# print(False or False)
# print("-" * 10)
# print(not True)
# print(not False)

# print("-" * 10)
# print(20 > 10 or -10 > 10)
# print(20 > 10 and not (-10 > 10))
# print("-" * 20)
# result = False and print("This will not print!")
# result = True or print("This will never print!")
# print(result)

# debug = False 
# debug and print('Detailed logs ----')

# # Identity 
# a = [1, 2, 3]
# b = [1, 2, 3]
# print(a is b)
# print(a == b)

# a = "python"
# b = "python"
# print(a is b)
# print(id(a))
# print(id(b))

# num1 = 300
# num2 = 300
# print(num1 is num2) #256

# numbers1 = [1, 2, 3]
# numbers2 = [1, 2, 3]
# print(numbers1 is numbers2)
# print(numbers1 is not numbers2)

fruits = ["apple", "banana", "grape"]
print("apple" in fruits)
print("Banana" in fruits)
print("orange" not in fruits)

print("-" * 40)

text = "This is a cool text, cats and dogs"
print("cat" in text)
print("dogs" in text)
print("text " in text)

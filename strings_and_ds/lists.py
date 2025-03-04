# Lists - Collection of items
# It is ordered
# It is mutable - you can modify it
# Dynamic in size, and dynamic in types

# ------------------------------------------------------
# Creation
my_list = []
another_my_list = list()

print(my_list, type(my_list))
print(another_my_list, type(another_my_list))

# Supply values
numbers = [1, 2, 3, 4, 5, 6]
fruits = ["apple", "banana"]

# Mixed data types
mixed = [1, True, "hello", 3.14]
print(mixed)

# Nested Lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix)

# supply values at creation with strings or range() function
chars = list("hello")
print(chars)
new_numbers = list(range(1, 11))
print(new_numbers)

# Combining Lists
list1 = [10, 20, 30]
list2 = [40, 50, 60]
combined = list1 + list2
print(combined)

# Replicate lists
zeros = [100] * 5
print(zeros)

# repeated genearation of lists
my_list = [10, 20, 30]
repeated = my_list * 3
print(repeated)

# Accessing elements from a list
fruits = ["apple", "banana", "orange", "cherry", "date", "grape"]
#           0          1         2         3        4        5
# Indexing
first = fruits[0]
second = fruits[1]

# negative indexing
last = fruits[-1]
second_last = fruits[-2]

print(first, type(first))
print(second, type(second))
print(last, type(last))
print(second_last, type(second_last))


# print(fruits[20])

# Slicing
fruits = ["apple", "banana", "orange", "cherry", "date", "grape"]
#           0          1         2         3        4        5

# Basic Slicing [start:end]
first_three = fruits[0:3]
first_three = fruits[:3]

middle = fruits[1:5]
print(first_three)
print(middle)

# ommit any of the indices
print(fruits[:5])
print(fruits[2:])
print(fruits[:])

shallow_copy = fruits[:]  # shallow copy of the list - TODO explain


fruits = ["apple", "banana", "orange", "cherry", "date", "grape"]
#           0          1         2         3        4        5
# Using Step [start:end:step]
every_second = fruits[::2]
print(every_second)
reverse_list = fruits[::-1]
print(reverse_list)

# Nested lists - 2D
matrix = [
    #  0      1       2
    ["one", "two", "three"], # 0
    ["four", "five", "six"], # 1
    ["seven", "eight", "nine"], # 2
]
# row
# column

print(matrix[0])
print(matrix[1])
print(matrix[2])

# Access specific elements form a matrix
print(matrix[0][1])
print(matrix[1][2])
print(matrix[2][0])

# Modifying and Adding
fruits = ["apple", "banana", "orange", "cherry", "date", "grape"]

# changing one value
first = fruits[0]
fruits[0] = "apricot"

# changing multiple values
# fruits[1:3] = ["blueberry", "blackberry"]
fruits[1:2] = ["blueberry", "blackberry", "dragonfruit"]

# clean up the list
# fruits[:] = []

print(fruits)

# Adding elements with methods
fruits = ["apple", "banana", "orange", "cherry", "date", "grape"]

# append - adding to the end of the list
fruits.append("blackberry")
print(fruits)

fruits.insert(0, "apricot")
print(fruits)

# extends extracts the elements from the list provided and adds them to the current list
fruits.extend(["strawberry", "pinapple"])
print(fruits)
# append adds the given list as a whole element
fruits.append(["strawberry", "pinapple"])
print(fruits)

# Removal
fruits = ["apple", "banana", "orange", "cherry", "date", "grape"]

fruits.remove("cherry") # it removes by value
print(fruits)

# del keyword
# del fruits[0]
# print(fruits)

# pop() method - return back the element removed
last = fruits.pop()
print(last)
print(fruits)

second = fruits.pop(1)
print(second)
print(fruits)

# clear
fruits.clear()
print(fruits)

fruits = ["apple", "banana", "orange", "cherry", "date", "grape"]

numbers = [3, 1, 6, 4, 7, 2, 9, 8, 5]
print(f"Before Sort: {numbers}")

numbers.sort()

print(f"After Sort: {numbers}") # Asc

numbers.sort(reverse=True)
print(f"After Sort Reverse: {numbers}") # desc


words = ["python", "is", "awesome"]
words.sort()
print(words)

words.sort(key=len)
print(words)

# reverse
words.reverse()
print(words)


fruits = ["apple", "banana", "orange", "cherry",
          "date", "date", "grape", "banana", "banana"]
# count()
number_of_babana = fruits.count("banana")
print(number_of_babana)

# index()
index = fruits.index("banana")
index = fruits.index("banana", 3)
print(index)

# in
print("banana" in fruits)
print("bana" in fruits)


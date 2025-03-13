# # List Comprehension
# names = ["Bob", "Mark", "Larry", "Lisa", "Bart"]

# # We need to create a new list with all names upper case
# # Traditional way with loops:
# modified_names = []

# for name in names:
#     upper_name = name.upper()
#     modified_names.append(upper_name)

# print(modified_names)

# # We can achieve this with a List comprehension
# modified_names_compr = [name.upper() for name in names]
# print(modified_names_compr)


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

# # Traditional with for loop
# even_numbers = []
# for num in numbers:
#     if num % 2 == 0:
#        even_numbers.append(num)
# print(even_numbers)

# # List comprehension
# even_numbers_compr = [num for num in numbers if num % 2 == 0]
# print(even_numbers_compr)

# Dictionary Comprehension

# words = ["cat", "dog", "elephant", "fish", "bird", "horse"]

# # Traditional Way
# hash_table = {}

# for word in words:
#     hash_table[word] = len(word)

# print(hash_table)

# # Dict comprehension
# hash_table_compr = {word: len(word) for word in words}
# print(hash_table_compr)


# numbers = [1, 1, 1, 2, 2, 3, 4, 4, 4, 5, 6, 7, 7, 7, 8, 9, 9, 9, 10, 10, 10]

# even_numbers = set()
# for num in numbers:
#     if num % 2 == 0:
#         even_numbers.add(num)
# print(even_numbers)

# # Set Comprehension
# unique_even_numbers_compr = {num for num in numbers if num % 2 == 0}
# print(unique_even_numbers_compr)
# import sys

# squares_list = [num**2 for num in range(1000)]
# print(sys.getsizeof(squares_list)) # bytes int
# print(sys.getsizeof(squares_list) / 1024)

# squares_list_gen = (num**2 for num in range(1000))
# print(sys.getsizeof(squares_list_gen)) # bytes int
# print(sys.getsizeof(squares_list_gen) / 1024)

# # next will give you next value of generator object
# print(next(squares_list_gen))
# print(next(squares_list_gen))
# print(next(squares_list_gen))
# print(next(squares_list_gen))
# print(next(squares_list_gen))
# print(next(squares_list_gen))
# print(next(squares_list_gen))

# sum_of_squares = sum(num**2 for num in range(1000))
# print(sum_of_squares)

# print(min(num**2 for num in range(100, 1000)))
# print(max(num**2 for num in range(100, 1000)))


# fruits = ["apple", "banana", "pear", "grape", "apple"]

# unique_fruits = {fruit.capitalize() for fruit in fruits}
# print(unique_fruits)

# fruit_table = {fruit.capitalize(): len(fruit) for fruit in fruits}
# print(fruit_table)


# nested_list = [
#     ["Jack", "Mark", "Bob"],
#     ["Nick", "Lisa", "Tom"],
#     ["Bart", "Alice", "Larry"]
# ]
# print(nested_list[0][1])

# flattened_names = [element for row in nested_list for element in row]
# print(flattened_names)
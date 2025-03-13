# # Loops
# # Looping over a List
# fruits = ["apple", "banana", "cherry"]

# for fruit in fruits:
#     print(f"I like {fruit}s")

# # looping Over a String
# text = "python"
# for letter in text:
#     print(letter, end="-")
# print()

# # looping over a range of numbers
# for i in range(10):
#     print(i, end=" ")
# print()

# # loopint over a list by using index and element value
# for i, fruit in enumerate(fruits):
#     print(f"{i + 1}. {fruit.capitalize()}")

# # looping over a string with index to control the logic
# text = "python"
# for i, letter in enumerate(text):
#     if i == len(text) - 1:
#         print(letter, end="\n")
#     else:
#         print(letter, end="-")

# student = {"name": "Alice", "age": 40, "city": "New York"}
# for key in student:
#     print(f"key = {key} and value = {student[key]}")


# # Range function
# for i in range(6):
#     print(i, end=" ")
# print()

# for i in range(2, 6):
#     print(i, end=" ")
# print()

# for i in range(0, 10, 2):
#     print(i, end=" ")
# print()

# for i in range(5, 0, -1):
#     print(i, end=" ")
# print()

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# for i in range(len(numbers)):
#     print(numbers[i], end=" ")
# print()

# While Loop
# count = 1
# while count <= 10:
#     print(f"Count: {count}")
#     count += 1

# expenses = []
# user_command = ""

# while user_command != "quit":
#     user_input = input("Enter an expense to add to the list or 'quit':")
#     if user_input == "quit":
#         user_command = user_input
#     elif user_input.isdigit():
#         expenses.append(float(user_input))
#     else:
#         print("Invalid input. Please enter a number or 'quit':")

# print(f"Expenses: {expenses}")


# for i in range(11):
#     if i == 5:
#         print("Breaking at 5")
#         break
#     print(i, end=" ")
# print("After the break of the loop...")


# for i in range(11):
#     if i % 2 == 0:
#         continue
#     print(i, end=" ")
# print()
# print("After continue in the loop")

# for i in range(11):
#     if i % 2 == 0:
#         print(f"{i} is even")
#         if i == 6:
#             break
#     else:
#         print(f"{i} is odd")
# else:
#     print("Finished iterating over the whole range!")


# search_term = input("What language you are serching for: ")
# languages = ["Java", "C++", "JavaScript", "Ruby", "Python", "Rust"]

# for lang in languages:
#     if lang == search_term:
#         print(f"Found {search_term}")
#         break
# else:
#     print(f"{search_term} not found in the list.")

# # Nested Loops
# for leg in range(4):
#     print(f"Assembling leg {leg + 1}")
#     for screw in range(3):
#         print(f"-- Screw {screw + 1}")

# matrix = [
#     [10, 12, -3],
#     [40, 5, 6],
#     [-72, 18, 99]
# ]

# print("Print all numbers that are higher than 5")
# for row in matrix:
#     for element in row:
#         if element > 5:
#             print(element, end=" ")
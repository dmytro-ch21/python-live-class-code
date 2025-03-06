print("Sets Practice")

# Create sets with literals
# list use - []
# sets use - {}
# dictionaries also use - {}

# numbers = {1, 2, 3, 4, 5, 1}
# colors = {"red", "green", "yellow"}
# mixed_set = {1, 1.5, True, "blue"}
# print(numbers, type(numbers))
# print(colors, type(colors))
# print(mixed_set, type(mixed_set))

# # be careful with empty sets creation
# empty_set = set()
# empty_dict = {}
# print(empty_set, type(empty_set))
# print(empty_dict, type(empty_dict))

# # converts strings and lists to set
# list_to_set = set([1, 2, 3, 4, 5, 1, 2])
# print(list_to_set)

# string_to_set = set("hello")
# print(string_to_set)

# # Immutability of the elements
# immutable_set = {10, "hello", (1,2,3)}
# print(immutable_set)

# invalid_set = {[1,2,3]}
# print(invalid_set)

# set is mutable
# nested_set = {{1,2,3}, {4,5,6}}
# print(nested_set)

# print(hash([1,2,3]))
# print(hash("hello"))
# print(hash(100))
# print(hash(3.14))
# print(hash(True))


# All the data types and structures can be either: Immutable or Mutable
# what does it mesn:
# mutable means that we can modify a place in the memory -> [] | ----*------ |
# immutable -> one the object is created and stored in memory that object cannot be modified

# mutable - not hashable
# immutable - can be hashed and optimized

# Create a simple set with strings
# fruits = {"apple", "banana", "pear"}
# print(fruits)

# # adding to the set - single items
# fruits.add("orange")
# print(fruits)

# duplicates will be ignored
# fruits.add("orange")
# print(fruits)

# adding multiple items
# fruits.update(["blueberry", "blackberry"])
# print(fruits)

# create a new set
# numbers = {1, 2, 3}
# numbers.update("hello world")
# print(numbers)

# fruits = {"apple", "banana", "pear", "orange", "watermelon", "melon"}

# # discard and remove
# fruits.discard("pear")
# print(fruits)

# # discard doesnt produce an error when item is not in the set
# fruits.discard("new fruit")
# print(fruits)

# fruits.remove("apple")
# print(fruits)

# remove does raise an error is element not in the set
# fruits.remove("new fruit")
# print(fruits)

# it removes an arbritrary element
# there no guearantee that specific element will be removed
# item_popped = fruits.pop()
# print(item_popped)

# Operations with sets:


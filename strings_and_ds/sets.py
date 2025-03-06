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

# # Operations with sets:
# set_a = {1, 2, 3, 4, 5}
# set_b = {4, 5, 6, 7, 8}

# # Union -> unite them together
# union_set_func = set_a.union(set_b)
# union_set_pipe = set_a | set_b

# print(f"union_set_func: {union_set_func}")
# print(f"union_set_pipe: {union_set_pipe}")

# # Intersection - finds elements common in both sets
# intersection_set_func = set_a.intersection(set_b)
# intersection_set_apm = set_a & set_b
# print(f"intersection_set_func: {intersection_set_func}")
# print(f"intersection_set_apm: {intersection_set_apm}")

# # Difference - finds the elements that are in first set but not in second
# diff_set_func = set_a.difference(set_b)
# diff_set_min = set_a - set_b

# print(f"diff_set_func: {diff_set_func}")
# print(f"diff_set_min: {diff_set_min}")

# # Symmetric - finds element those that are in either set but both
# symmetric_set_func = set_a.symmetric_difference(set_b)
# symmetric_set_carrot = set_a ^ set_b

# print(f"symmetric_set_func: {symmetric_set_func}")
# print(f"symmetric_set_carrot: {symmetric_set_carrot}")


# # indexing and slicing not available in sets
# numbers = {1, 2, 3, 4, 5}
# # print(numbers[1]) # not valid - TypeError
# # print(numbers[::-1]) # not valid - TypeError

# # testing memebership
# fruits = {"apple", "banana", "pear", "orange", "watermelon", "melon"}

# print("apple" in fruits)
# print("pear" in fruits)
# print("bear" in fruits)


# print("Find unique elements: ")
# survey_responses = ["cat", "dog", "fish", "bird", "cat", "cat", "dog", "dog"]
# print(f"survey responses: {survey_responses}")

# unique_pets = set(survey_responses)
# print(f"unique pets: {unique_pets}")

# # Finding common things 
# alice_favorites = ["pizza", "sushi", "tacos", "pasta"]
# bob_favorites = ["burgers", "sushi", "curry", "pasta"]

# print(f"Alice likes: {alice_favorites}")
# print(f"Bob likes: {bob_favorites}")
# print(f"Food they both like: {set(alice_favorites) & set(bob_favorites)}\n")

# print(f"Food they like different: {set(alice_favorites) ^ set(bob_favorites)}\n")

# print(f"Food Bob likes different than Alice: {set(bob_favorites) - set(alice_favorites)}\n")

# print(f"Food Alice likes different than Bob: {set(alice_favorites) - set(bob_favorites)}")

# fruits = {"apple", "banana", "pear", "orange", "watermelon", "melon"}
# allergic_to = {"apple", "melon"}

# print(f"All Fruits in Fridge: {fruits}")
# print(f"Allergic To: {allergic_to}")
# print(f"Fruits To Keep: {fruits - allergic_to}")





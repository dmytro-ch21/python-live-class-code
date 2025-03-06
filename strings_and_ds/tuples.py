print("================ Tuples ================")

# [] - Lists
# {} - Dict
# {1, }, set() - Set
# () - Tuple

# # Creating Tuples
# # Empty Tuples
# empty_tuple = ()
# empty_tuple_constr = tuple()
# print(empty_tuple, type(empty_tuple))

# singleton_wrong = (10)
# print(f"singleton_tuple_value: {type(singleton_wrong)}")

# singleton_tuple = (10,)
# print(f"singleton_tuple: {type(singleton_tuple)}")

# singleton_tuple = 10,  # parenthesys are optional, comma is essential
# print(f"singleton_tuple: {type(singleton_tuple)}")

# # Multiple values in tuple
# simple_tuple = (1, 2, 3)
# mixed_tuple = (1, 2.5, True, ["one", "two"], "hello")
# nested_tuple = (1, (2, 3), [4, 5, 6], {7, 8, 9})

# print(simple_tuple)
# print(mixed_tuple)
# print(nested_tuple)

# # Tuple Packing
# packed_tuple = 10, 20, 30, 40, 50
# print(packed_tuple, type(packed_tuple))

# # Create tuples from iterable ds (set is not iterable)
# tuple_from_list = tuple(["a", "b", "c"])
# tuple_from_str = tuple("hello world")
# tuple_from_range = tuple(range(1, 11))

# print(tuple_from_list)
# print(tuple_from_str)
# print(tuple_from_range)

# # Accessing tuple elements
# coordinates = (10, 20, 30, 40, 50, 60)

# # Indexing
# print(f"Tuple: {coordinates}")
# print(f"Accest First Element: {coordinates[0]}")
# print(f"Accest Last Element: {coordinates[-1]}")
# print(f"Accest second to Last Element: {coordinates[-2]}\n")

# # Slicing
# print(f"Accest First Two Elements: {coordinates[:2]}")
# print(f"Everything but first: {coordinates[1:]}")
# print(f"Everything but last: {coordinates[:-1]}")
# print(f"Every second element: {coordinates[::2]}")
# print(f"Reversed Tuple: {coordinates[::-1]}")

# # Tuples Unpacking
# a, b, c, d, e, f = coordinates
# print(f"a={a} b={b} c={c} d={d} e={e} f={f}")

# first, *middle, last = coordinates
# print(f"first={first} middle={middle} last={last}")

# *beginnig, last = coordinates
# print(f"beginnig={beginnig} last={last}")

# first, *rest = coordinates
# print(f"first={first} rest={rest}")

# # Tuples are immutable on its own
# immutable_tuple = (1, 2, 3)
# print(f"Original Tuple: {immutable_tuple}")

# # immutable_tuple[0] = 5
# # new_tuple = (5,) + immutable_tuple[1:]
# # print(new_tuple)

# mutable_elements = (10, [1,2,3,4], "hello", {"name": "Bob"})
# print(mutable_elements)

# mutable_elements[1].append(10)
# print(mutable_elements)

# mutable_elements[3]["name"] = "Alice"
# print(mutable_elements)

# # Tuple Operations
# t1 = (1, 2, 3)
# t2 = (4, 5, 6)

# concat = t1 + t2
# print(concat)

# repeated = t2 * 5
# print(repeated)

# print(len(repeated))

# # membership testing 
# print(f"Is 2 in t1 {2 in t1}")
# print(f"Is 2 in t2 {2 in t2}")

# # Tuples have 2 functions count and index
# count_five = repeated.count(5)
# print(count_five)

# # Find specific index
# find_index_of_5 = repeated.index(5)
# print(find_index_of_5)




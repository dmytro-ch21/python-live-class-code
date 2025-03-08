# shallow copy and deep copy
# copies only the first level items, nested things will be referenced
# student1 = {
#     "name": "Mark",
#     "grades": [80, 100, 90]
# }

# student2 = student1.copy()
# student2["name"] = "Bob"

# student2["grades"][0] = 100

# print(student1)
# print(student2)

# deep copy
# we will need to import copy module
# import copy
# student1 = {
#     "name": "Mark",
#     "grades": [80, 100, 90]
# }

# student2 = copy.deepcopy(student1)
# student2["name"] = "Bob"

# student2["grades"][0] = 100

# print(student1)
# print(student2)

# const [items, setItems] = useState([]);

# ❌ items.push()
# ❌ items.pop()

# items = [
#     {
#         "name": "Bob",
#         "age": 44
#     }, 
#     {
#         "name": "mark",
#         "age": 45
#     },
# ]

# setItems([...items, {"name": "new name", "age": 11}])


# some_obj = {
#     "key1": "value1",
#     "key2": "value2",
#     "key3": "value3",
#     "key4": "value4",
#     "key5": "value5",
# }

# {...some_obj, "key6", "value6"}

# import pprint

# items = [
#     {
#         "name": "Bob",
#         "age": 44
#     }, 
#     {
#         "name": "mark",
#         "age": 45
#     },
# ]

# items.append({"name": "Bart", "age": 33})

# items = [*items, {"name": "Lisa", "age": 40}]
# pprint.pprint(items, width=2)

# some_obj = {
#     "key1": "value1",
#     "key2": "value2",
#     "key3": "value3",
#     "key4": "value4",
#     "key5": "value5",
# }

# some_obj["key6"] = "value6"

# pprint.pprint(some_obj)
# print("-" * 40)
# some_obj = {**some_obj, "key7": "value7"}
# pprint.pprint(some_obj)


# if statements 
print("Starting the flow")

condition = False

if condition:
    print("It was True!")


print("Continuing the flow")

x = 11
if x > 10: 
    print(f"x={x} is really more than 10")
    
age = 16

if age > 18:
    print("You can get in with someone older")
elif 18 <= age > 21: 
    print("You can get in")
else: 
    print("go back home!")
# def add(x, y):
#     return x + y

# print(add(10, 20))

# add_lambda = lambda x, y: x + y
# print(add_lambda(100, 200))

# result = (lambda num: num * 2)(10)
# print(result)


# numbers = [10, 20, 30, 40, 50]
# doubled_numbers = list(map(lambda num: num * 2, numbers))
# print(doubled_numbers)


# fruits = ["oranges", "grapes", "cherries"]
# cap_fruits = list(map(lambda fruit: fruit.capitalize(), fruits))
# print(cap_fruits)

# dict_fruits = list(map(lambda fruit: {fruit.capitalize(): len(fruit)} , fruits))
# print(dict_fruits)

# Example Filter
from functools import reduce
users = [
    {"name": "Alice", "age": 25, "active": True},
    {"name": "Bob", "age": 17, "active": True},
    {"name": "Charlie", "age": 40, "active": False},
    {"name": "Lisa", "age": 18, "active": True},
]


adult_active_users = list(filter(
    lambda user: user.get("age") >= 18 and user.get("active"),
    users
))

for user in adult_active_users:
    print(
        f"Name: {user.get("name")}, Age: {user.get("age")}, Active: {user.get("active")}")


# Example Reduce
numbers = [10, 20, 30, 40, 50]
sum_result = reduce(lambda x, y: x + y, numbers)
print(sum_result)


# Sorting
fruits = ["Apple", "Pear", "Banana", "Grape",
          "Watermelon", "Pinapple", "Dragonfruit"]

sorted_fruits = sorted(fruits, reverse=True)
sorted_fruits = sorted(fruits, key = lambda fruit: len(fruit))
sorted_fruits = sorted(fruits, key = lambda fruit: fruit[1])
print(sorted_fruits)

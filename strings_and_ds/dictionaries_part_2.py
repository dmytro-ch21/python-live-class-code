import pprint
# dictionary1 = {}
# dictionary2 = dict()

# print(dictionary1, type(dictionary1))
# print(dictionary2, type(dictionary2))

# # create with literals

# dict_literals = {
#     "key" : "value",
#     "key2" : "value2",
# }
# print(dict_literals)

# dict_constr = dict(key="value", key_2="value")

# # accessing the dictionaries
# import pprint
# student = {
#     "name": "John Doe",
#     "id": 12345,
#     "courses": ["HTML", "CSS", "JS", "Python"],
#     "grades": {
#         "HTML":  100,
#         "CSS":  90,
#         "JS":  79,
#         "Python":  99,
#         "letter_system": ["A", "A", "B", "A"]
#     },
# }

# # print(student)

# # import a module pprint
# pprint.pprint(student)
# print()
# print(student["name"])
# print(student.get("name"))

# # print(student["unknown_key"]) # error
# print(student.get("unknown_key"))
# # default value returned only if keyt is not found
# print(student.get("unknown_key", "Undefined"))

# print(student["courses"][3])
# print(f"HTML: {student["grades"]["HTML"]}")
# print(f"Letter Grade One: {student["grades"]["letter_system"][0]}")

# letter = student.get("grades").get("letter_system")[2]
# print(letter)


# # modification of objects 

# product = {
#     "id": 1001,
#     "name": "Laptop",
#     "price": 999.99,
#     "is_stock": True
# }

# # pprint.pprint(product, width=10)

# # dict is mutable you can add new items later ater creation 
# product["brand"] = "TechCo"
# product["model"] = "XP500"

# pprint.pprint(product, width=10)
# print("-" * 20)

# # update existing ones
# product["price"] = 799.80
# product["is_stock"] = False

# pprint.pprint(product, width=10)

# # update function allows you to add and update multiple items at the time
# product.update({
#     # change exiting items
#     "price": 855.90,
#     "is_stock": True,
#     # create at the same time
#     "color": "silver",
#     "warranty": 2,
#     "new_item": False
# })

# print("-" * 20)
# pprint.pprint(product, width=10)

# # removal
# # pop() - will return you the value back of specified key...
# removed_warranty_value = product.pop("warranty", 2)

# print("-" * 20)
# pprint.pprint(product, width=10)
# print("-" * 20)
# print(removed_warranty_value)

# # if you want to handle the error while pooping you could provide a default value. -> if the key not found, instead of giving error it will return the default value.
# removed_warranty_value = product.pop("invalid_key", False)
# print(removed_warranty_value)
# print("-" * 20, end="\n\n")

# removed_item = product.popitem()
# pprint.pprint(product, width=10)
# print("-" * 20)
# print(removed_item)

# pprint.pprint(product, width=10)
# print("-" * 20)

# del product["id"]

# pprint.pprint(product, width=10)
# print("-" * 20)



# other methods 
settings = {
    "theme": "dark",
    "font_size": 12,
    "notifications": True,
    "language": "en"
}

# pprint.pprint(settings, width=10)

# keys = settings.keys()
# # values = settings.values()
# # items = settings.items()

# print(f"Keys: {keys}")
# # print(f"Values: {values}")
# # print(f"Items: {items}")

# settings["volume"] = 80
# print(f"Keys: {keys}")

# print(list(keys))

# # Membership check 
# has_theme = "theme" in settings
# has_color = "color" in settings

# print(has_theme)
# print(has_color)

# # setdefault - 
# settings.setdefault("theme")
# settings.setdefault("volume", 50)
# pprint.pprint(settings, width=10)
































# There are only few mutable:
# Dict, List, Set







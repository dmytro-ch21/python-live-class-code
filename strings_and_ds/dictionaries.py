# Create an empty dictionary
# empty_dict = {}
# empty_dict_alt = dict()

# print(empty_dict, type(empty_dict))
# print(empty_dict_alt, type(empty_dict_alt))

# person = {
#     "name": "John Doe",
#     "age": 30,
#     "city": "New York"
# }

# print(f"Person Dictionary: {person}")

# # different way of creating the dict
# colors = dict(red="#FF0000", black="#000", white="#FFF")
# print(colors)

# # using immutable structures to combine a dict
# items = dict([("apple", 1.88), ("pear", .9), ("orange", 2.4)])

# print(items)

# mixed_keys = {
#     10: "answer",
#     "pi": 3.14,
#     True: "boolean",
#     (1, 2): "tuple"
# }

# print(mixed_keys)

# Accessing the data in dictionaries 

student = {
    "name" : "John Doe",
    "id" : 12345,
    "courses" : ["CSS", "HTML", "JavaScript", "Python"],
    "grades" : {
        "CSS": 87,
        "HTML": 100,
        "JavaScript": 77,
        "Python": 80
    }
}

print(student)

name = student["name"]
courses = student["courses"]
grade = student["grades"]["Python"]

print(f"Student Name: {name}")
print(f"Student Active Course: {courses[0]}")
print(f"Student Python Grade: {grade}")

# access some key that doesnt exist 
# print(student["last_name"]) - KeyError

id_number = student.get("id")
age = student.get("age")
age_default = student.get("id", False)

print(f"Students ID: {id_number}")
print(f"Students Age: {age}")
print(f"Students Age: {age_default}")


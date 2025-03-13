# List Comprehension
names = ["Bob", "Mark", "Larry", "Lisa", "Bart"]

# We need to create a new list with all names upper case
# Traditional way with loops:
modified_names = []

for name in names:
    upper_name = name.upper()
    modified_names.append(upper_name)

print(modified_names)

# We can achieve this with a List comprehension
modified_names_compr = [name.upper() for name in names]
print(modified_names_compr)
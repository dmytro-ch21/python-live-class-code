# Example One

# Function that takes one argument and returns a transformation of it as new object
def double_it(num):
    return num ** 2

# Data is separated from functions
# We do not mutate it
numbers = [10, 20, 30, 40, 50]

# map function syntax: map(function, data)
# the map will return you back a map object that you will need to cast it to a list/dict/tuple etc...
doubled_numbers = list(map(double_it, numbers))
print(doubled_numbers)


# Example Two

# The function that will be applied for each word
def translate_to_spanish(word):
    # have a dictionary with words
    fruit_translation = {
        "Apples": "Manzanas",
        "Oranges": "Naranjas",
        "Bananas": "Plátanos",
        "Grapes": "Uvas",
        "Pineapples": "Piñas",
        "Cherries": "Cerezas",
        "Strawberries": "Fresas",
    }
    # return back the value of a found key
    # if key not present return the word itself
    return fruit_translation.get(word, word)

# Data is separated from function
# This list will not mutate (we intentionally do it)
fruits = ["oranges", "grapes", "cherries"]

# Function to capitalize the words
def capitalize(word):
    return word.capitalize()

# Here we map over the list of fruits and standartize them by capitalizing it
# You also can apply trimming to avoid any extra spaces
fruits_capitalized = list(map(capitalize, fruits))

print(fruits_capitalized)

# Now we can use the standartized list to translate to spanish
spanish_fruit_translation = list(map(translate_to_spanish, fruits))
# another approach is you can nest map() functions (Not recommended because the code gets harder to read)
spanish_fruit_translation = list(map(translate_to_spanish, list(map(capitalize, fruits))))

print(spanish_fruit_translation)


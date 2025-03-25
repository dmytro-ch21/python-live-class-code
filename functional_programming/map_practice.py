def double_it(num):
    return num ** 2


numbers = [10, 20, 30, 40, 50]

doubled_numbers = list(map(double_it, numbers))
print(doubled_numbers)


def translate_to_spanish(word):
    fruit_translation = {
        "Apples": "Manzanas",
        "Oranges": "Naranjas",
        "Bananas": "Plátanos",
        "Grapes": "Uvas",
        "Pineapples": "Piñas",
        "Cherries": "Cerezas",
        "Strawberries": "Fresas",
    }
    return fruit_translation.get(word, word)

fruits = ["oranges", "brapes", "cherries"]

def capitalize(word):
    return word.capitalize()

fruits_capitalized = list(map(capitalize, fruits))

print(fruits_capitalized)

spanish_fruit_translation = list(map(translate_to_spanish, fruits))
spanish_fruit_translation = list(map(translate_to_spanish, list(map(capitalize, fruits))))

print(spanish_fruit_translation)


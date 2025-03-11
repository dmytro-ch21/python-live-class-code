# Loops

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(f"I like {fruit}s")
    
text = "python"
for letter in text:
    print(letter, end="-")    
print()

for i in range(10): 
    print(i, end=" ")
print()

for i, fruit in enumerate(fruits): 
    print(f"{i + 1}. {fruit.capitalize()}")
    
    
text = "python"
for i, letter in enumerate(text):
    if i == len(text) - 1:
        print(letter, end="\n")    
    else:    
        print(letter, end="-")
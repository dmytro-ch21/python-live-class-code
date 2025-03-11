# Loops
# Looping over a List
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(f"I like {fruit}s")
    
# looping Over a String    
text = "python"
for letter in text:
    print(letter, end="-")    
print()

# looping over a range of numbers
for i in range(10): 
    print(i, end=" ")
print()

# loopint over a list by using index and element value
for i, fruit in enumerate(fruits): 
    print(f"{i + 1}. {fruit.capitalize()}")
    
# looping over a string with index to control the logic    
text = "python"
for i, letter in enumerate(text):
    if i == len(text) - 1:
        print(letter, end="\n")    
    else:    
        print(letter, end="-")
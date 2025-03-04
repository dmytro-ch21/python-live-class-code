# Built In functions to operate on numbers
result = abs(-10)
result = round(10.88784)
result = round(10.88784, 3)
result = max(10, 20, 33, -90, -1)
result = min(10, 20, 33, -90, -1)
result = sum([10, 20, 33, -90, -1])

# use the math module
import math

result = math.sqrt(25)
result = math.floor(33.99)
result = math.ceil(33.01)
result = math.pow(2, 3)

# use rnadom for random numbers
import random
result = random.random() # 0.0 == 1.0
result = random.randint(1, 100)
result = random.choice(["red", "blue", "green", "balck", "yellow"])
fruits = ["apple", "banana", "plum", "orange"]
result = fruits
# modifying the list itself 
random.shuffle(fruits)

print(f"result: {result}")
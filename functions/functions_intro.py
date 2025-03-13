# Creating a basic function
# def greet():
#     print("Hello, world!")
#     print("This is my first function in Python!")

# # invoke, run, call, execute
# greet()
# greet()
# greet()
# greet()

# # type notation in python that is optional

# def greet() -> None:
#     print("Hello, world!")
#     print("This is my first function in Python!")

# print("Hello", "World")

# def greet(name):
#     print(f"Hello, {name}!")


# greet("Bob")
# greet("Mark")
# greet("Lisa")

# # type notations


# def greet(name: str) -> None:
#     print(f"Helloooo, {name}!")


# greet("Bob")


# def add(a, b):
#     print(f"a + b = {a + b}")
    
# def add(a: int, b: int) -> None:
#     print(f"a + b = {a + b}")    
    
# add(10, 20)


# def greet_with_age(name: str, age: int) -> None:
#     print(f"Hello, I'm {name}, and I'm {age} years old.")
    
# greet_with_age("Lisa", 30)    
# greet_with_age(30, "Lisa")

# def add(a, b):
#     print(f"performing ... {a} + {b} = {a + b}")
#     # sum = a + b variable return
#     return a + b

# def bundle_together(a, b, c, d):
#     # my_tuple = (a, b, c, d)
#     return a, b, c, d
    
    
# def add(a: int, b: int) -> int:
#     return a + b

# def bundle_together(a: int, b: int, c: int, d: int) -> tuple:
#     # my_tuple = (a, b, c, d)
#     return a, b, c, d
     
# result = bundle_together(10, 0, -10, 2)
# print(result, f"type: {type(result).__name__}")    

# sum = add(100, -20)
# print(sum)

# def calculate(x, y):
#     x = 10
#     y = 20
#     print(f"x = {x} and y = {y}")
    
# calculate(10, 20)

# print(x)   # Error variable not defined 
# print(y)   # Error variable not defined


# message = "I'm global scope variable"

# def demonstate_scope():
#     print("We are in function scope")
#     print("We are accessing a global variable:")
#     print(f"It says: {message}")
    
    
# def try_reassign_global_variable():
#     # we create a completely new varibale 
#     # it is part of the local scope
#     # any changes to it will be not reflected to global variable
#     message = "I'm a local variable"
#     print(f"Here is message from local scope: {message}")   
    
# count = 0

# def try_modify_the_global_variable():
#     count = count + 1
#     print(count)
    
# # try_modify_the_global_variable() # cannot modify directly
     
    
# demonstate_scope()
# try_reassign_global_variable()

# print(f"The global variable state: {message}")



count = 0
 
# def increment():
#     count = count + 1
#     print(count)
     
# # increment() 

# def increment_correctly(inc: int):
#     global count
#     count = count + inc
#     print(f"current count from function: {count}")
    
# increment_correctly(2)
# increment_correctly(3)   
# increment_correctly(5)   
# increment_correctly(8)      

# print(f"Global variable count: {count}")   

def increment(c: int) -> int:
    return c + 1

count = increment(count)
count = increment(count)
count = increment(count)
count = increment(count)
count = increment(count)
count = increment(count)
count = increment(count)
print(count)

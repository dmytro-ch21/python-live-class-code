# print("Arguments")

# def my_function():
#     """ This function is super simple, just prints no args """
#     print("No args")

# def my_function_with_args(first: str, second: str):
#     """
#     This function accepts two positional arguments
#     Args:
#         first: str
#         second: str
#     Returns:
#         None
#     """
#     print(f"{first} {second}")

# my_function()

# print(my_function_with_args.__doc__)


# # keyword arguments
# my_function_with_args("Hello", "World")
# my_function_with_args(second="World", first="Hello")

# # def new_function():
# #     pass

# def greet(name="Unknown"):
#     print(f"Hello, {name}")

# greet("Alice")
# greet()

# def create_profile(name: str, age: int = 0, country: str = "Unknown"):
#     print("------ Profile Info -------")
#     print(f"Name: {name},\nAge: {age},\nCountry: {country}")

# create_profile("Alice")
# create_profile("Bob", 30)
# create_profile("Mark", 40, "USA")

# # Arbitrary Arguments
# def sum_all(*args: int) -> int:
#     sum = 0
#     for num in args:
#         sum += num
#     return sum

# result = sum_all(10, 20, 30, 40, 50)
# print(result)


# def team_info(capitan, subs, *players) -> None:
#     print("-------- Team -------")
#     print(f"Capitan: {capitan}")
#     print(f"Players: {players}")
#     print(f"Substitude: {subs}")

# team_info("Mark", "Bob", "John", "Nick", "Larry")


# def user_profile(**user_info):
#     print("--------- User Info ---------")
#     for key in user_info:
#         print(f"{key} {user_info[key]}")


# user_profile(name="Alice", age=25, country="USA",
#              city="Miami", address="123 Street")


# def process_data(required, *args, **kwargs):
#     print(f"Required: {required}")
#     print(f"Arbitrary Positional Args: {args}")
#     print(f"Arbitrary Keyword Args: {kwargs}")

# # Note: Remember when you mix the arguments the order matters!
# # First goes positinal arguments
# # Then default ones
# # Then Arbitrary Args
# # Then Abitrary Keword Args
# process_data("Bob", 1, 2, 3, 4, 5, 6, b=20, c=30)


def main():
    def greet():
        print("Hello World from Main Function!!!")

    greet()


main()


def outer_function(x):
    """This is the outer function scope"""
    def inner_function(num):
        """This is the inner function and it has it's own scope"""
        return num * 100

    result = inner_function(x)
    return f"Output is: {result}"


print(outer_function(50))


# Closure - Is achieved when you have a nested function inside of outer function, and the outer function has a state that is used by inner function

# def create_counter():
#     count = 0
#     print("Increment Count: ")
#     count += 1
#     return count
    

# Closure example with cache of the counter
# def create_counter():
#     count = 0
    
#     def increment():
#         # It references the variable to parent/outer function
#         nonlocal count
#         count += 1
#         return count
    
#     return increment

# counter = create_counter()
# counter() # 1
# counter() # 2
# counter() # 3 
# counter() ...
# counter() ...
# counter() ...

# # Access the function object closure cell (state of the closure)
# print(counter.__closure__[0].cell_contents)


# Infinite Recursive Call between 2 functions
# def function_a():
#     print("Executing Function A")
#     print("--Calling Function B")
#     function_b()
    
# def function_b():
#     print("Executing Function B")
#     print("--Calling Function A")
#     function_a()
    
# function_a()


# def print_hello(count):
#     for _ in range(count):
#         print("Hello World!")


# # print_hello(10) 

# def print_hello_rec(count):
#     # base case
#     if count == 0:
#         return
#     print("Hello World!")
#     print_hello_rec(count - 1)
    
# print_hello_rec(5)
    
# def factorial(n):
#     total = 1
#     for i in range(1, n+1):
#         print(i)
#         total *= i
#     return total

# result = factorial(5)
# print(result)


# # x! = x * (x - 1)! 
# def factorial(n):
#     if n <= 1:
#         return 1
#     return n * factorial(n - 1)

# result = factorial(5)
# print(result)

# some_func() - definition first before the invokation

# def some_func():
#     print("Ima a function!")






 
    








print("Arguments")

def my_function():
    print("No args")

def my_function_with_args(first: str, second: str):
    print(f"{first} {second}")

# my_function("hey")

# keyword arguments
my_function_with_args("Hello", "World")
my_function_with_args(second="World", first="Hello")

# def new_function():
#     pass

def greet(name="Unknown"):
    print(f"Hello, {name}")

greet("Alice")
greet()

def create_profile(name: str, age: int = 0, country: str = "Unknown"):
    print("------ Profile Info -------")
    print(f"Name: {name},\nAge: {age},\nCountry: {country}")

create_profile("Alice")
create_profile("Bob", 30)
create_profile("Mark", 40, "USA")

# Arbitrary Arguments 
def sum_all(*args) -> int:
    sum = 0
    for num in args:
        sum += num
    return sum 
        
result = sum_all(10, 20, 30, 40, 50)       
print(result)


def team_info(capitan, subs, *players) -> None:
    print("-------- Team -------")
    print(f"Capitan: {capitan}")
    print(f"Players: {players}")
    print(f"Substitude: {subs}")
    
team_info("Mark", "Bob", "John", "Nick", "Larry")




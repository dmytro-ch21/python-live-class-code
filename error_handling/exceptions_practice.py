# Syntax Errors
# print("Hello World"
# print("Hello"."world")

# 
# input_1 = input("Enter one input")
# input_2 = input("Enter another input")

# print(int(input_1) + input_2)


# print("Welcome! Lets divide 2 numbers:")


# num1 = int(input("Enter Number One:"))
# num2 = int(input("Enter Number Two:"))

# try:
#     print(f"The division of {num1} / {num2} is {num1 / num2}")
# except:
#     print("Division by 0 not possible. Please provide a non 0 number...")    

# print("Proceeding with execution...")
# try:
#     number = int(input("Enter a number:\n")) # potential problem
#     result = 100 / number # potential problem
#     print(f"{number} / 100 = {result}")
# except ValueError:
#     print("Input Error! Not Good :(")    
# except ZeroDivisionError:
#     print("Division by 0 not possible!")       
    
# print("Program Resumes....")   

# try:
#     number = int(input("Enter a number:\n")) # potential problem
#     result = 100 / number # potential problem
#     print(f"{number} / 100 = {result}")
# except (ValueError, ZeroDivisionError):
#     print("Input Error! Not Good :(")   
    
# print("Program Resumes....")     

# try:
#     result = 100 / 0 # potential problem
# except ZeroDivisionError as e:
#     print("Input Error! Not Good :(")
#     print(f"Error message: {str(e)}")
#     print(f"Error: {type(e).__name__}")   
    
# print("Program Resumes....")

# def get_number() -> int:
#     try:
#         number = int(input("Enter a number: \n"))
#     except ValueError as e:
#         print("That's not a valid number!")
#         print(f"{type(e).__name__} with message: {str(e).upper()}")
#     else:
#         print(f"You entered: {number}")
#         return number
#     finally:
#         print("Function execution completed! All clean ups completed!")
            
            
# get_number()            

# def calculate_average(numbers):
#     if not numbers:
#         raise ValueError("Cannot calculate average based on an empty list!")
#     return sum(numbers) / len(numbers)


# nums = [10, 22, 3, 2, 11, 2, 3, 88]

# try:
#     result = calculate_average([])
# except ValueError as e:
#     print("Added the error to logger!")
#     raise # Rerasing is when you want to provide handling of an error partially
# else:
#     print(f"Average: {result}")
    
# class InsufficientFundsError(Exception):
#     pass

# def withdraw(amount, balance):
#     if amount > balance:
#         raise InsufficientFundsError(f"Not enought funds to withdraw ${amount} with balance ${balance}")
#     return balance - amount

# try:
#     result = withdraw(1000, 2000)
# except InsufficientFundsError:
#     print("Not enought money!")
    
# print(f"Money Left: ${result}")

# try:
#     result = withdraw(1000, 500)
# except InsufficientFundsError:
#     print("Not enought money!")
    
# print(f"Money Left: ${result}")  

class ConnectionError(Exception):
    """Raisen when unable to connect to a database"""
    def __init__(self, host, port, message=False):
        self.host = host
        self.port = port
        if not message:
            message = f"Failed to connect to the database with url: {self.host}:{self.port}"
        super().__init__(message)   

def connect_to_db(connection):
    if connection:
        print("Access DB and retrieve data...")
        return True
    else:
        raise ConnectionError("81.978.836", "8080", "Lol😂")
  
  
  
try:    
    connect_to_db(False)    
except:
    print("Error captured but not handled properly! Dont ever suppress the error as right here!!!")    
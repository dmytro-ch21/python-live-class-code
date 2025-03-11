# Simple If - Else statement
# temperature = 65

# if temperature >= 70:
#     clothing = "t-shirt"
# else:
#     clothing = "sweater"

# print(f"You should wear a {clothing}")

# Multiple elif statements

# income, based on the income you fall into a specific tax_bracket - A,B,C,D
# BAD
# income = 90000

# if income > 0:
#     tax_bracket = "A - 11%"
# elif income > 20000:
#     tax_bracket = "B - 16%"
# elif income > 50000:
#     tax_bracket = "C - 21%"
# else:
#     tax_bracket = None

# print(f"Tax Bracket for {income} is: {tax_bracket}")

# # GOOD
# income = 10000

# if income > 50000:
#     tax_bracket = "C - 21%"
# elif income > 20000:
#     tax_bracket = "B - 16%"
# elif income > 0:
#     tax_bracket = "A - 11%"
# else:
#     tax_bracket = None

# print(f"Tax Bracket for {income} is: {tax_bracket}")

# has_ticked = False
# bag_weight = 10

# if user has ticket print ticket verified and then check luggage

# if has_ticked:
#     print("Ticket verified.")

#     if bag_weight <= 23:
#         print("Check - In Completed!")
#         print("Have a nice flight!")
#     else:
#         print("Bag is too heavy.")
#         print("Please pay excess baggage fee.")

# else:
#     print("You need a ticket to check - in. Please get one!")

# if has_ticked and bag_weight <= 23:
#     print("Ticket verified.")
#     print("Check - In Completed!")
#     print("Have a nice flight!")
# elif has_ticked:
#     print("Bag is too heavy.")
# else:
#     print("You need a ticket.")

# Scopes
# variables defined in if, for, while scopes are still visible outside of the scope as long as the body of those statements has been executed

# x = 4
# if x > 5:
#     y = 20
#     print(f"Inside if block: x = {x} and y = {y}")

# print(f"Outside of if statement, x = {x}")

# everything is correct - if y gets initialized then it will be visible
# the issue is present when the if statement condition is False
# In that case y is not defined and not visible outside
# print(f"Outside of if statement, y = {y}")


# Ternary Operator

# age = 21

# if age >= 21:
#     status = "Adult"
# else:
#     status = "Minor"    

# print(f"Status: {status}")


# # Rewrite with ternary 
# age = 21

# status = "Adult" if age >= 21 else "Minor"
# print(f"Status: {status}")

# # expression
# print(f"You are {"old enough" if age >= 21 else "too young"} to drink in US.")

# # chaining ternary
# temp = 15 # C
# # freezing, cold, mild, warm
# weather = "freezing" if temp < 0 else "cold" if temp < 10 else "mild" if temp < 20 else "warm"
# print(f"Weather is {weather}")

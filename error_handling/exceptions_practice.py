# Syntax Errors
# print("Hello World"
# print("Hello"."world")

# 
# input_1 = input("Enter one input")
# input_2 = input("Enter another input")

# print(int(input_1) + input_2)


print("Welcome! Lets divide 2 numbers:")


num1 = int(input("Enter Number One:"))
num2 = int(input("Enter Number Two:"))

try:
    print(f"The division of {num1} / {num2} is {num1 / num2}")
except:
    print("Division by 0 not possible. Please provide a non 0 number...")    

print("Proceeding with execution...")
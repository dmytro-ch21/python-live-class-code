# int - integer - holds whole numbers
number = 100
number = -202
number = 12673617152673651276512367431257456772613
print(number, type(number))

# float - decimal numbers
price = 12.99
price = -12.99
price = 0.0
price = 125365123564.238754672378546273657823658926758296784236589239
print(price, type(price))
print(0.1 + 0.2 == 0.3)

# complex
complex_num = 3 + 10j
print(complex_num.real)
print(complex_num.imag)

# boolean - holds only True or False (Yes, No) (1,0)
is_cold = True
is_subscribed = False 
print(f"It is cold outside: {is_cold}")
print(f"User is subscribed: {is_subscribed}")

# NoneType - specifies that a variable doesnt hold anything at the time
empty_variable = None
print(f"The variable is: {empty_variable}")

# strings - a representation of a sequence of characters
single_quotes = 'Im in sigle quotes'
double_quotes = "Im in double quotes"
multi_line = """This is a multi line string
This line should be in the new line 
That's the last one!
"""
multi_line_single = '''Same thing here
Multi line single quotes
'''
print(f"Single Quotes: {single_quotes}")
print(f"Double Quotes: {double_quotes}")
print(f"Multi-line string: {multi_line}")
print(f"Multi-line string: {multi_line_single}")


raw_string = r"C:\Users\User\Documents"
print(raw_string)

# creating strings with constructor
new_str = "New String First"
new_str = str("New String Here")
print(new_str, type(new_str))




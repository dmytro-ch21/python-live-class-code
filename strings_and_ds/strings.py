# Strings - are a sequence of characters
# Immutable - Objects cannot be changed

text = 'This is a string'
text = "This is a string"
text = """This is a string"""
print(text)

# ------------------------------------------ 

# String concatenations - option 1
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print("full_name: ", full_name)

# String concatenations - option 2 (implicit)
hello = "Hello " "World!"
long_statemnt = ("This is very long text."
                 " To be frank this is really long."
                 " It cannot be any longer than this.")

print(hello)
print(long_statemnt)

# ------------------------------------------ 
# f-strings
f_name = "Bob"
l_name = "Marley"
country = "Jamaica"
statement = f"{f_name} {l_name} - {country}"
print(statement)

# ------------------------------------------ 
# String formatting with format() method - old way 
name = "Bob"
age = 25

greeting = "My name is {0} and I'm {1} years old. To repeat name is {0}".format(name, age)
print(greeting)

# ------------------------------------------ 
# Percent Formatting - % (legacy way)
legacy_formmated_string = "Name: %s Age: %d" % (name, age)
print(legacy_formmated_string)

# ------------------------------------------ 
# Formatting numbers in f-strings
number = 35124365.3623423
print(f"{number:,}")
print(f"{number:.2f}")
print(f"{10:#b}")
print(number)

# ------------------------------------------ 
txt = "hello"
print(txt, id(txt))
new_txt = "hello"
print(new_txt, id(new_txt))

# immutable
# name = "Mark"
# name[0] = "D"
# print(name)

# ------------------------------------------ 
# Indexing
# string is a seq characters and they are indexed
# hello
# 01234
text = "Python Programming"
print(text[0])
print(text[7])
# print(text[20])

# length - 1 = (18 - 1) = 17
print(text[-1])
print(text[-2])

# ------------------------------------------ 






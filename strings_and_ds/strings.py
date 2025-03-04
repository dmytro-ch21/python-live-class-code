# Strings - are a sequence of characters
# Immutable - Objects cannot be changed

# text = 'This is a string'
# text = "This is a string"
# text = """This is a string"""
# print(text)

# # ------------------------------------------

# # String concatenations - option 1
# first_name = "John"
# last_name = "Doe"
# full_name = first_name + " " + last_name
# print("full_name: ", full_name)

# # String concatenations - option 2 (implicit)
# hello = "Hello " "World!"
# long_statemnt = ("This is very long text."
#                  " To be frank this is really long."
#                  " It cannot be any longer than this.")

# print(hello)
# print(long_statemnt)

# # ------------------------------------------
# # f-strings
# f_name = "Bob"
# l_name = "Marley"
# country = "Jamaica"
# statement = f"{f_name} {l_name} - {country}"
# print(statement)

# # ------------------------------------------
# # String formatting with format() method - old way
# name = "Bob"
# age = 25

# greeting = "My name is {0} and I'm {1} years old. To repeat name is {0}".format(
#     name, age)
# print(greeting)

# # ------------------------------------------
# # Percent Formatting - % (legacy way)
# legacy_formmated_string = "Name: %s Age: %d" % (name, age)
# print(legacy_formmated_string)

# # ------------------------------------------
# # Formatting numbers in f-strings
# number = 35124365.3623423
# print(f"{number:,}")
# print(f"{number:.2f}")
# print(f"{10:#b}")
# print(number)

# # ------------------------------------------
# txt = "hello"
# print(txt, id(txt))
# new_txt = "hello"
# print(new_txt, id(new_txt))

# # immutable
# # name = "Mark"
# # name[0] = "D"
# # print(name)

# # ------------------------------------------
# # Indexing
# # string is a seq characters and they are indexed
# # hello
# # 01234
# text = "Python Programming"
# print(text[0])
# print(text[7])
# # print(text[20])

# # length - 1 = (18 - 1) = 17
# print(text[-1])
# print(text[-2])

# ------------------------------------------
# String Slicing [start:end] (end is exclusive)
text = "Python Programming"

print(text[0:8]) # Python P
print(text[0:100]) # no error just till the end
print(text[:7]) # Python
print(text[0:]) # Python Programming
print(text[:]) # Python Programming
print(text[6:]) 
print(text[:-5])

text = "Python Programming"
# Using Steps
# [start:end:step] # Python Programming [::1]
print(text[::1])
print(text[::2])
print(text[::3])
print(text[::-1]) # reverses the string
print(text[::])


string = "python"
print(len(string))
# get first half
print(string[:3])
print(string[:len(string) // 2])
# get second half
print(string[len(string) // 2:])

# functions - methods (methods belong to objects)
# print() # function
# "hello".format() # method

sentence = "Python is one of the most popular languages in the world. Python is cool."
# print(dir(sentence)) # get all possible methods for senstence object

print(sentence.upper())
print(sentence.lower())
print(sentence.replace("Python", "Programming"))
print(sentence.replace("o", "0"))
print(sentence.split()) # def is space

# methods returning bools
print(sentence.startswith("Py"))
print(sentence.startswith("one", 10)) # offset
print(sentence.endswith("cool."))

# getting info on elements - searching 
print(sentence.find("Python")) 
print(sentence.find("Python", 10))

# joining - creating a string from sequences
result = "".join(["a", "p", "p", "l", "e"])
print(result)

# other useful methods 
sentence = "Python is one of the most popular languages in the world. Python is cool."

count_of_python = sentence.count("Python")
count_of_o = sentence.count("o")
print(count_of_python)
print(count_of_o)

print("10abc".isalnum())
print("abc".isalpha())
print("10".isdigit())
print("10".isascii())
print(" ".isspace())

sentence = "python is one of the most popular LANGUAGES in the world. python is cool."

# Capitalization
print(sentence.capitalize())
print(sentence.title())














# word = "     Python      "
# print(f">{word}<") 
# print(f">{word.strip()}<")




# print(sentence)







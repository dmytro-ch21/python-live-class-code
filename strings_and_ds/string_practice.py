# practice
# Lets take an input as a full name (first name and last name)
# Also take an input as a preffered domain
# Based on that generate 3 different usernames
# And 3 dofferent emails

full_name = input("Privide you first and last name space separated: \n")
domain = input("What domain you prefer (e.g. gmail.com, aol.com): \n")

first_name, last_name = full_name.split() 

print("=============== USERNAMES =================")
print(f"{first_name.lower()}{last_name.lower()}")
print(f"{first_name.lower()}_{last_name.lower()}")
print(f"{first_name.lower()}.{last_name.lower()}")

print("=============== EMAILS =================")
print(f"{first_name.lower()}{last_name.lower()}@{domain}")
print(f"{first_name.lower()}_{last_name.lower()}@{domain}")
print(f"{first_name.lower()}.{last_name.lower()}@{domain}")


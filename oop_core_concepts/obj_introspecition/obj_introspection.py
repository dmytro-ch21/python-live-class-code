class Person:
    def __init__(self, f_name, l_name, dob, ssn):
        self.f_name = f_name
        self._l_name = l_name
        self._dob = dob
        self.__ssn = ssn
    
    def get_full_name(self):
        return f"{self.f_name.title()} {self._l_name.title()}"
    
    def get_last_4_ssn_digits(self):
        return f"*{self.__ssn[-4:]}"
    
    def __str__(self):
        return f"{self.get_full_name()} - {self._dob} - {self.get_last_4_ssn_digits()}"
    
    
class User(Person):
    pass

class Guest(Person):
    pass
    
bob = Person("Bob", "Smith", "15-09-1980", "123-321-1231")
print(bob)

# Object Introspection - is ability to inspect an object in different ways
# get the type
print(type(bob))
# get only the class type name
print(type(bob).__name__)
# get the class/type
print(bob.__class__)
# get only the class type name
print(bob.__class__.__name__)

if bob.__class__.__name__ == "Person":
    print("Hey, Person! Welcome :)")

# print(dir(bob))

# for member in dir(bob):
#     print(member)
    
# get members of the class that are custom defined
for member_of_class in dir(bob):
    if not member_of_class.startswith("__"):  
        print(member_of_class) 
        
print(bob.f_name)

if hasattr(bob, "name"):
    print(bob.name)
    
print(hasattr(bob, "name"))    
print(hasattr(bob, "f_name"))    
print(hasattr(bob, "_Person__ssn"))
print(getattr(bob, "f_name"))

# you can check if an object is an instance of a specifi class 
print(isinstance(bob, Person))
print(isinstance(bob, list))


user = User("Nick", "Doe", "15-09-1980", "233-221-0000")
gues = Guest("Guest", "Doe", "15-09-1980", "233-000-0000")

print(issubclass(User, Person))
print(issubclass(User, Guest))
print(issubclass(Guest, Person))
print(issubclass(Guest, object))

 
# all classes inherit from object in python
from datetime import date

# parent base class
class Animal:
    
    # class level variable in base class
    general_property = "Animal"
    
    def __init__(self, name, breed, species):
        self.name = name # public 
        self.breed = breed # public 
        self._species = species # protected
        # one property of date 
        self.__date_recieved = date.today() # private
                
    def make_sound(self):
        print("Animal is making a generic sound...")
        
    def get_info(self):
        print(f"----------- {self._species} ------------")        
        print(f"Name: {self.name}")        
        print(f"Breed: {self.breed}")
        print(f"Recieved: {self.__date_recieved}")          
        print(f"---------------------------")        
        

# we inherit by using () and type at class definition
# child / derived class inheriting from Animal
class Dog(Animal):
    # by default the subclass will call the init constructor automatically
    
    # you can add new functionality to the derived class
    def sniff(self):
        print(f"{self.name} is busy sniffing...")

    # in addition you can ovverride things like properties and methods
    general_property = "Dog"
    
    # override the make sound method
    # override - means provide different implementation
    def make_sound(self):
        print("Woof!")
        
# Another child class
class Cat(Animal):
    def __init__(self, name, breed, color):
        # Option 1 - Legacy
        # Animal.__init__(self, name, breed, "Cat")
        # Option 2  - Modern
        super().__init__(name, breed, "Cat")
        # additional property in subclass
        self.color = color
        
    def sleep(self):
        print(f"{self.name} is busy slipping...")
        
    def make_sound(self):
        print("Meow...")
        
    # extend the parent get_info function    
    def get_info(self):
        super().get_info()
        print(f"Color: {self.color}")
        print(f"----------------------------")
        
animal = Animal("Max", "Shepard", "Dog")
animal.make_sound()
animal.get_info()
print(animal.general_property)

my_dog = Dog("Buddy", "Husky", "Dog")
my_dog.get_info()
my_dog.sniff()
my_dog.make_sound()
print(my_dog.general_property)

my_cat = Cat("Viskas", "British Shorthair", "Grey")
my_cat.get_info()
my_cat.make_sound()




class Animal:
    def __init__(self, name):
        self._name = name
        
    def speak(self):
        pass
    
class Cat(Animal):
    def speak(self):
        return f"{self._name} says meow!"
    
class Dog(Animal):
    def speak(self):
        return f"{self._name} says woof!"
    
class Cow(Animal):
    def speak(self):
        return f"{self._name} says moo!"
    
animals = [Cat("Max"), Dog("Buddy"), Cow("Bassie")]

for animal in animals:
    print(animal.speak())
    
    
def what_is_the_sound(animal):
    print("------- sound like ---------")
    print(animal.speak())
    
cat = Cat("Max")
dog = Dog("Buddy")
cow = Cow("Bassie") 
 
what_is_the_sound(cat)     
what_is_the_sound(dog)     
what_is_the_sound(cow)     
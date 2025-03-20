class Dog():
    
    dog_count = 0
    species = "Canis"
    
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        Dog.dog_count += 1
        print(f"New Dog Object created: (name={name}, breed={breed})")
        print(f"Species: {Dog.species}")
         
    def bark(self):
        print(f"{self.name} is barking loud!")    
        
    def pretty(self):
        print(f"Dog(name={self.name}, breed={self.breed})")
        
        
dog_1 = Dog("Buddy", "Reriever")       
dog_2 = Dog("Max", "Shepard")

dog_1.pretty()
dog_2.pretty()

print(f"Dog Count: {Dog.dog_count}")
 
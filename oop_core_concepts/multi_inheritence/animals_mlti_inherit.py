class Animal:
    def __init__(self, name):
        self.name = name
        
    def eat(self):
        print(f"{self.name} is eating")    
        
    def slepp(self):
        print(f"{self.name} is sleeping")
        
    def colliding_method(self):
        print("Colliding method: Animal Implementation")
        
    
class FlyingCreture:
    def __init__(self, speed, wing_span):
        self.speed = speed
        self.wing_span = wing_span
        
    def fly(self):
        print(f"Flying with {self.speed} mph speed and {self.wing_span} inch wingspan")
        
    def colliding_method(self):
        print("Colliding method: FlyingCreture Implementation")    
        
class Bat(Animal, FlyingCreture):               
    def __init__(self, name, speed, wing_span):
        Animal.__init__(self, name)
        FlyingCreture.__init__(self, speed, wing_span)
            
bruce = Bat("Bruce", 40, 15)
print(bruce.name)
print(bruce.speed)
print(bruce.wing_span)

# inherited from Animal
bruce.eat()
bruce.slepp()
# inherited form FlyingCreature
bruce.fly()

bruce.colliding_method()


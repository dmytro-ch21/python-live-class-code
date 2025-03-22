class Boat():
    def move(self):
        print("Boat sails on water")
        
class Car():
    def move(self):
        print("Car drives on road")
        
class Airplane():
    def move(self):
        print("Airplance flies in the air")  
        
def how_it_moves(vehicle):                      
    vehicle.move()
    
boat = Boat()    
car = Car()
airplane = Airplane()
    
how_it_moves(boat)    
how_it_moves(car)  
how_it_moves(airplane)


boat == car

print(boat)
print(bool(boat))


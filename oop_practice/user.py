class User:
    # this is a class level variable
    count = 0
    current_year = 2025
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        User.count += 1
        
    def pretty(self):
        print(f"User(name={self.name}, age={self.age})")
       
    # methods denoted with decorator classmethod can operate on class metadata, for example access constructor or class level variables    
    @classmethod    
    def get_total_users(cls):
        return cls.count
    
    # with cls object you have access to constructor
    # that means you can create some logic and after create object with computed data
    @classmethod
    def create_user_from_birth_year(cls, name, birth_year):
        age = User.current_year - birth_year # 2025 - 1980 = 45 
        return cls(name, age)
        
           
user1 = User("Alice", 20)        
user2 = User("Bob", 50)

user1.pretty()
user2.pretty()

print(User.get_total_users())

user3 = User.create_user_from_birth_year("Nick", 1999)
user3.pretty()
        
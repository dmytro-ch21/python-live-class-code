# ========================== EXAMPLE 1 ==========================
# Regular apprach - creating manually getters and setters 
# class User: 
#     def __init__(self, name, year):
#         self.__name = name
#         self.__year = year
        
#     def get_name(self):
#         return self.__name
    
#     def get_year(self):
#         return self.__year
    
#     def set_year(self, new_year):
#         self.__year = new_year
    
#     def set_name(self, new_name):
#         self.__name = new_name
    
    
# user = User("Alice", 1990)   

# user.set_name("Alice Baker") 
# user.set_year(1992) 

# user_name = user.get_name()
# user_year = user.get_year()

# print(user_name)
# print(user_year)
    

# user = User("Alice", 1990)    
# print(user.name)  
# obj._ClassName__property
# print(user._User__year)    
# user._User__year = 2020
# print(user._User__year)  



# ========================== EXAMPLE 2 ==========================
# Using property decorator 
# once you set a property 
# you can create setters by using the property name.setter
class User: 
    def __init__(self, name, year):
        self.__name = name
        self.__year = year
        self.__username = "Not Set"
        
    @property    
    def name(self):
        return self.__name
    
    @property
    def year(self):
        return self.__year
    
    @property
    def username(self):
        return self.__username
    
    @username.setter
    def username(self, new_username):
        self.__username = new_username
    
    @year.setter
    def year(self, new_year):
        self.__year = new_year
    
    @name.setter
    def name(self, new_name):
        self.__name = new_name 
          
user = User("John Doe", 1980)
print(user.name)
print(user.year)
print(user.username)

user.name = "Alice"
user.username = "aliceusername"
print(user.name)
print(user.username)
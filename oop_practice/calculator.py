class Calculator:
    
    name = "Simple Calculator"
    
    # static methods allow you to create methods that are not accessing cls or self objects
    # They are simply helper or utility functions!
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def multiply(x, y):
        return x * y
    
    @staticmethod
    def is_even(x):
        return x % 2 == 0
    

print(Calculator.add(10, 20))    
print(Calculator.multiply(10, 20))    
print(Calculator.is_even(100))
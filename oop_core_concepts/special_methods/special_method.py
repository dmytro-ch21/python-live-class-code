# There different objects that are built in and act upon differen fulity in special way
# for example when we pass a list to print() function it prins the content of it
# when we call the len() on list it gives me the length of how many elements we have inside of the list
# all these can be implemented for your custom type/class
# numbers = [1, 2, 3, 4, 5]
# print(numbers) # __str__
# print(len(numbers)) # __len__
# print(bool(numbers)) # 

# class Car:
#     def __init__(self, make, model):
#         self.make = make
#         self.model = model
      
# my_car = Car("BMW", 2025)        
# print(my_car)
# print(bool)
# # print(len(my_car))


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = 0
    
    # String representation for print() function
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    # Representation for dev with repr function
    def __repr__(self):
        return f"Book({self.title}, {self.author}, {self.pages})"
        
    # length logic, based on which we calculate the len()
    def __len__(self):
        return self.pages
    
    # how do we specify if our book/object if truthy or falsy
    def __bool__(slef):
        return slef.pages > 0
    
    # we can make our object iterable
    def __iter__(self):
        return self
    
    # in addition to iter we need to define what happens with next() iteration
    def __next__(self):
        # we need to specify when we will stop iteration
        # a must is to raise an Error StopItteration
        # this is how the loop will know where to stop
        if self.current_page >= self.pages:
            self.current_page = 0
            raise StopIteration
        self.current_page += 1
        return f"Page {self.current_page}"
    
book = Book("Python Programming", "John Smith", 350)
book2 = Book("C#", "John Doe", 100)
book3 = Book("Not Started", "Unknown", 0)

print(book)      
print(book2)

print(repr(book)) 
print(repr(book2)) 

print(len(book))
print(len(book2))

print(bool(book))
print(bool(book2))
print(bool(book3))

for page in book:
    if page == "Page 100":
        print("Found It!")  
        break
    print(page)




        



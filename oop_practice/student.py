# define a class
class Student:
    # we will use constructor method __init__ to constratuc and populate data to object we are instantiating
    # you can have as many paramas as you need
    # you can combine different ones as: positional, arbitrary, kwars, or defaults for optional params
    # self is a placeholder for the object that python will pass over automatically
    def __init__(self, name, student_id=0):
        self.name = name
        self.student_id = student_id
        # sometimes you need some properties automatically defined 
        # regrdless of the constructor, you can do it as well 
        self.courses = []
    
    # methods in a class should have at least one parameter taking self instance
    def say_hello(self):
        print(f"Hello, I'm a Student! {self}")
        
        

# ======================= Practice =======================
# instantiation - instance (object)
new_student = Student("Alice", 101)
# access the methods of an object with dot notation
new_student.say_hello()
# also we can access the properties/attributes of the object same way 
print(new_student.name)
print(new_student.student_id)

# if we have same variables we can later access them and manipulate
new_student.courses.append("Python")
new_student.courses.append("JS")

print(new_student.courses)

# In this case each object maintains its own state 
# here self object plays a crutial role to achieve it
new_student_2 = Student("Mark")
new_student_2.say_hello()
print(new_student_2.name)
print(new_student_2.student_id)



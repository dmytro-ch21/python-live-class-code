# absolute path 
from path_practice.package_1 import module_1

# relative path (..) go to parent
from ..package_1 import module_1

def function_from_pck_2():
    print("function_from_pck_2")
    module_1.function_from_pck_1()
    
    
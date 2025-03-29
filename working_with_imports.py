import random
print(random.random())

# we can use from and import for specif functions/modules
from random import random, shuffle
print(random())
print(shuffle([10, 20, 30]))

# if the modules are lengthy we can give them an alias
# that alias can utilized in code instead of the original module name
import random as rd
print(rd.random())

# Import the utilities modules 
from utilities import api_interactions_v1 as api
api.api_v1_request()

# not recommended since it introduces a lot of confusion
from random import *
print(random())


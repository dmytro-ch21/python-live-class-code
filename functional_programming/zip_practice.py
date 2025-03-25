import itertools 

# Having different lists 
names = ["Alice", "Bob", "Bard", "Nick", "Lisa"]
ages = [25, 55, 44, 30, 15, 10, 20, 30, 40]
cities = ["Boston", "New York", "Miami", "Charlotte", "Las Olas"]

# we can zip them (group same idex items in a tuple)
people = list(zip(names, ages, cities))
print(people)

for person in people:
    print(person)
    
# You can use the zip object as a dict    
name_to_age_dict = dict(zip(names, ages))
print(name_to_age_dict)

# you could zip with longest list length 
# for this we will need to import itertools and use zip_longest()
people_two = list(itertools.zip_longest(names, ages, cities, fillvalue="NA"))
print(people_two)


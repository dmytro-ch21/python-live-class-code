import os

current_folder = os.getcwd()
print(f"We are at: {current_folder}")

# see what is inside of your folder 
path = '/Users/dmytrochobotar/FSD/python-projects/playground'
contents = os.listdir(path)
for item in contents:
    print(item)
    
# create a new folder
os.mkdir('testing_folder')




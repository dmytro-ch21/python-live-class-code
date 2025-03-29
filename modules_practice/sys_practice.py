import sys

# print(f"Python version: {sys.version}")
# print(f"Python version: {sys.version_info}")
# print(f"OS: {sys.platform}")

print(f"Program/File Name: {sys.argv[0]}")
print(f"Other Ags: {sys.argv[1:]}")

if sys.argv[1] == "INFO":
    print("Configuring the project to run in INFO mode....")
else:
    print("Configuring the project to run in DEBUG mode....")    
    print(f"Python version: {sys.version}")   
    print(f"Python version: {sys.version_info}")   
    print(f"OS: {sys.platform}")   



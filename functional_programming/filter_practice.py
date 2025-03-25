users = [
    {"name": "Alice", "age": 25, "active": True},
    {"name": "Bob", "age": 17, "active": True},
    {"name": "Charlie", "age": 40, "active": False},
    {"name": "Lisa", "age": 18, "active": True},
]

def is_acceptable(user):
    return user.get("age") >= 18 and user.get("active")
    
adult_active_users = list(filter(is_acceptable, users))

for user in adult_active_users:
    print(f"Name: {user.get("name")}, Age: {user.get("age")}, Active: {user.get("active")}")
    
print(users)


    
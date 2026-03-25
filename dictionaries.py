# Dictionaries are collections of key-value pairs.
# Each key must be unique and immutable, while values can be any type.

# Creating a dictionary
print("\n--- CREATING A DICTIONARY ---")
my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
print(my_dict)

# Accessing values
print("\n--- ACCESSING VALUES ---")
print(my_dict["name"])  # prints: Alice

# Adding a new key-value pair
print("\n--- ADDING A NEW KEY-VALUE PAIR ---")
print(my_dict)
my_dict["profession"] = "Engineer"
print(my_dict)

# Modifying an existing value
print("\n--- MODIFYING AN EXISTING VALUE ---")
print(my_dict)
my_dict["age"] = 26
print(my_dict)

# Removing a key-value pair
print("\n--- REMOVING A KEY-VALUE PAIR ---")
print(my_dict)
del my_dict["city"]
print(my_dict)

# Iterating through dictionary keys and values
print("\n--- ITERATING THROUGH DICTIONARY ---")
for key, value in my_dict.items():
    print(f"{key}: {value}")

# Using items()
print("\n--- USING ITEMS() TO ITERATE ---")
another_dict = {"a": 1, "b": 2, "c": 3}
for key, value in another_dict.items():
    print(f"Key: {key}, Value: {value}")

# Checking if a key exists
print("\n--- CHECKING IF A KEY EXISTS ---")
if "name" in my_dict:
    print("Name is in the dictionary")

# Getting a value safely (returns None if key doesn't exist)
print("\n--- GETTING A VALUE SAFELY ---")
print(my_dict.get("city"))

# To change a key, add new key and remove old one
print("\n--- CHANGING A KEY ---")
print(my_dict)
my_dict["first_name"] = my_dict.pop("name")
print(my_dict)

# Using pop() to remove a specific key
print("\n--- USING POP() TO REMOVE A SPECIFIC KEY ---")
print(my_dict)
age_value = my_dict.pop("age")  # removes 'age' and returns its value
print(f"Removed age: {age_value}")
print(my_dict)

# Using popitem() to remove the last inserted item
print("\n--- USING POPITEM() TO REMOVE THE LAST INSERTED ITEM ---")
last_item = my_dict.popitem()
print(my_dict)
print(f"Removed last item: {last_item}")
print(my_dict)

# Using update() to add multiple items at once
print("\n--- USING UPDATE() TO ADD MULTIPLE ITEMS AT ONCE ---")
print(my_dict)
my_dict.update({"city": "Boston", "country": "USA"})
print(my_dict)

# Dictionary with different value types
print("\n--- DICTIONARY WITH DIFFERENT VALUE TYPES ---")
complex_dict = {
    "numbers": [1, 2, 3],
    "info": {"height": 170, "weight": 65},
    "active": True
}
print(complex_dict)

# Copying a dictionary
print("\n--- COPYING A DICTIONARY ---")
print(my_dict)
my_copy = my_dict.copy()
print(my_copy)

# Clear dictionary
print("\n--- CLEARING A DICTIONARY ---")
print(my_dict)
my_dict.clear()
print(my_dict)
print()

# Common Python dictionary methods

my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

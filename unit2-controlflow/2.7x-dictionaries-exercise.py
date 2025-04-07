# Create a dictionary named my_dict containing the following key-value pairs:
# - "name": "Alice"
# - "age": 30
# - "city": "New York"
# - "is_student": False
# - "scores": [85, 90, 95]
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "is_student": False,
    "scores": [85, 90, 95]
}

# 1. Print the entire dictionary.
print("Entire dictionary:", my_dict)

# 2. Print the value associated with the key "name".
print("Value for 'name':", my_dict["name"])

# 3. Print all the keys in the dictionary.
print("All keys:", list(my_dict.keys()))

# 4. Update the value of "age" to 31 and print the updated dictionary.
my_dict["age"] = 31
print("Updated dictionary after changing 'age':", my_dict)

# 5. Add a new key-value pair "occupation": "Engineer" and print the updated dictionary.
my_dict["occupation"] = "Engineer"
print("Updated dictionary after adding 'occupation':", my_dict)

# 6. Print the length of the dictionary (number of key-value pairs).
print("Length of dictionary:", len(my_dict))


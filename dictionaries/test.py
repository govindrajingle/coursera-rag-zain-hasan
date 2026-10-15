# dictonaries store data in key:value pais. They are unordered, chanagable and don't allow duplicates

person = {"name": "Alice", "age": 25, "city": "New York"}
print(f"person dictionary: {person}")

# accessing value
print(f"name: {person["name"]}")

# adding new key value pair
person["email"] = "alice@hotmail.com"
print(f"updated person dictionary: {person}")

# Iterate over dictionary
for key, value in person.items():
    print(f"key: {key}\tvalue:{value}")

# iterate over keys only
for key in person:
    print(key)

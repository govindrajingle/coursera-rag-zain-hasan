# f strings are formatted string literals
# used to embed expressions inside string literal

name = "John"
age = 30
greeting = f"Hello, {name}. You are {age} years old."
print(greeting)

# Generate a string from as set of data ?
people = [
    {
        "name": "Alice Johnson",
        "age": 28,
        "email": "alice.johnson@example.com",
        "location": "New York, NY",
    },
    {
        "name": "Michael Smith",
        "age": 34,
        "email": "michael.smith@example.com",
        "location": "Los Angeles, CA",
    },
    {
        "name": "Emily Davis",
        "age": 22,
        "email": "emily.davis@example.com",
        "location": "Austin, TX",
    },
    {
        "name": "John Brown",
        "age": 45,
        "email": "john.brown@example.com",
        "location": "Chicago, IL",
    },
    {
        "name": "Sarah Wilson",
        "age": 31,
        "email": "sarah.wilson@example.com",
        "location": "Seattle, WA",
    },
]

temp = []
for person_info_dict in people:
    layout_string = f"name: {person_info_dict['name']}, age: {person_info_dict}"
    temp.append(layout_string)
formatted_string = "\n".join(temp)
print(formatted_string)

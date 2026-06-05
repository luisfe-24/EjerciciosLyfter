list_of_keys = ["access_level", "age"]

employee = {
    "name": "John",
    "email": "john@ecorp.com",
    "access_level": 5,
    "age": 28
}

for record in list_of_keys:
    if record in employee:
        employee.pop(record)

print(employee)

employees = [
    {"name": "Carlos", "email": "carlos@empresa.com", "department": "Ventas"},
    {"name": "Ana", "email": "ana@empresa.com", "department": "TI"},
    {"name": "Luis", "email": "luis@empresa.com", "department": "Ventas"},
    {"name": "Sofía", "email": "sofia@empresa.com", "department": "RRHH"},
]

grouped_employees = {}

for employee in employees:
    name = employee["name"]
    department = employee["department"]

    if department in grouped_employees:
        grouped_employees[department].append(name)

    else:
        grouped_employees[department] = [name]

print(grouped_employees)

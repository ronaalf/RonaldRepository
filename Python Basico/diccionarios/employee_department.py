employees = [
    {"name": "Carlos", "email": "carlos@corp.com", "department": "Sales"},
    {"name": "Ana", "email": "ana@corp.com", "department": "IT"},
    {"name": "Luis", "email": "luis@corp.com", "department": "Sales"},
    {"name": "Sofia", "email": "sofia@corp.com", "department": "HR"},
]

belongs_to = {}

for employee in employees:
    department = employee["department"]
    print(employee)

    if department not in belongs_to:
        belongs_to[department] = []
    belongs_to[department].append(employee)
    
print(belongs_to)
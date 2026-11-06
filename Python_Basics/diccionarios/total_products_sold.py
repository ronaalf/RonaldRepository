products = [
    {'name': 'Monitor', 'category': 'Electronic', 'price': 200},
    {'name': 'Keyboard', 'category': 'Electronic', 'price': 50},
    {'name': 'Chair', 'category': 'Furniture', 'price': 120},
    {'name': 'Table', 'category': 'Furniture', 'price': 180},
    {'name': 'Mouse', 'category': 'Electronic', 'price': 25},
]

total_category = {}

for product in products:
    category = product['category']
    price = product['price']
    
    if category not in total_category:
        total_category[category] = 0.0
    total_category[category] += price

print(total_category)

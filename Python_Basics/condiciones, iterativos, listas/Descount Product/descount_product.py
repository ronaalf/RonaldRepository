product_price = int(input("Enter the product price: "))

if product_price < 100:
    discount = product_price * 0.02
else:
    discount = product_price * 0.10

product_discount = int(product_price - discount)

print(f"The price wih the discount applied is {product_discount}")    
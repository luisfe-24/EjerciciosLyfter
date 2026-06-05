product_price = float(input("Escriba el precio de su producto: "))

if product_price < 100:
    discount = product_price * 0.02

else:
    discount = product_price * 0.1

final_price = product_price - discount
print(f"El precio final es de: {final_price}")

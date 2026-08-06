class Product:
    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.amount = amount


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        return

    def show_products(self):
        for product in self.products:
            print(
                f"Producto: {product.name} | Precio: {product.price} | Cantidad: {product.amount}")

    def calculate_total_value_of_inventory(self):
        total_value = 0
        for product in self.products:
            total_value += product.price * product.amount
        return total_value


product1 = Product("Mouse", 5000, 3)
product2 = Product("Teclado", 8000, 2)

my_inventory = Inventory()

my_inventory.add_product(product1)
my_inventory.add_product(product2)

my_inventory.show_products()
print(my_inventory.calculate_total_value_of_inventory())

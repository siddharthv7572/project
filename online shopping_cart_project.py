class Product:
    def __init__(self, name, price, quantity=1):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def total_price(self):
        return self.price * self.quantity
    
    def __str__(self):
        return f"{self.name}: ${self.price} x {self.quantity} = ${self.total_price():.2f}"

class ShoppingCart:
    def __init__(self):
        self.items = {}
    
    def add_item(self, product):
        if product.name in self.items:
            self.items[product.name].quantity += product.quantity
        else:
            self.items[product.name] = product
    
    def remove_item(self, name):
        self.items.pop(name, None)
    
    def update_quantity(self, name, quantity):
        if name in self.items:
            if quantity <= 0:
                self.remove_item(name)
            else:
                self.items[name].quantity = quantity
    
    def view_cart(self):
        if not self.items:
            print("Cart is empty.")
            return
        for product in self.items.values():
            print(product)
        print(f"Total: ${self.total_price():.2f}")
    
    def total_price(self):
        return sum(p.total_price() for p in self.items.values())

if __name__ == "__main__":
    cart = ShoppingCart()
    cart.add_item(Product("Laptop", 999.99))
    cart.add_item(Product("Mouse", 25.50, 2))
    cart.add_item(Product("Keyboard", 75.00))
    
    cart.view_cart()
    
    print(f"Checkout Total: ${cart.total_price():.2f}")

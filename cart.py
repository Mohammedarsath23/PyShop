class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: ${self.price:.2f}"


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"Added {item} to the cart.")

    def remove_item(self, item_name):
        for item in self.items:
            if item.name == item_name:
                self.items.remove(item)
                print(f"Removed {item} from the cart.")
                return
        print(f"Item '{item_name}' not found in the cart.")

    def total(self):
        return sum(item.price for item in self.items)

    def checkout(self):
        total_price = self.total()
        print("Your cart contains:")
        for item in self.items:
            print(item)
        print(f"Total amount: ${total_price:.2f}")
        self.items.clear()  # Clear the cart after checkout
        print("Cart has been cleared.")


# Example usage:
if __name__ == "__main__":
    cart = ShoppingCart()

    item1 = Item("Apple", 0.99)
    item2 = Item("Banana", 0.59)
    item3 = Item("Orange", 0.79)

    cart.add_item(item1)
    cart.add_item(item2)
    cart.add_item(item3)

    cart.checkout()  # Displays items and total, then clears the cart

    cart.remove_item("Banana")  # Trying to remove an item after checkout

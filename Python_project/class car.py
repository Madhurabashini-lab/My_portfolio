# fast food Restaurant
class Product:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description

    def display_details(self):
        print("\n--- Product Details ---")
        print(f"Product: {self.name}")
        print(f"Price: £{self.price:.2f}")
        print(f"Description: {self.description}")

# Create products
product1 = Product("Pizza", 20, "Cheese and tomato pizza")
product2 = Product("Burger", 12, "Beef burger with lettuce and tomato")
product3 = Product("Sandwich", 15, "Chicken and salad sandwich")
product4 = Product("Wrap", 13, "Chicken wrap with salad")

menu = [product1, product2, product3, product4]

order = []


# Display menu
print("===== MENU =====")

for number, product in enumerate(menu, 1):
    print(f"{number}. {product.name} - £{product.price:.2f}")


# Customer chooses a product
choice = int(input("\nEnter the number of the product you want: "))

if 1 <= choice <= len(menu):

    selected_product = menu[choice - 1]

    # Display product details
    selected_product.display_details()

    # Ask for quantity
    quantity = int(input("How many would you like? "))

    # Add product to order
    order.append({
        "product": selected_product,
        "quantity": quantity
    })

else:
    print("Sorry! That product is not on the menu.")


# Review order
print("\n===== YOUR ORDER =====")

total = 0

for item in order:
    product = item["product"]
    quantity = item["quantity"]

    item_total = product.price * quantity
    total += item_total

    print(f"{product.name} x {quantity} = £{item_total:.2f}")


print(f"Total: £{total:.2f}")


# fast food Restaurant
print ("===================")
print("      Wrap Stars     ")
print ("===================")

class product():
    def __init__ (self, name, price, description):
        self.name = name
        self.price = price
        self.description = description

    def display_details(self):
       print("----------product details-------------")
       print(f"The product name is: {self.name}") 
       print(f"The price of the product is: £{self.price}")
       print(f"Description: {self.description}")
       
product1 = product('pizza', 20, 'Cheese and Tomato pizza' )
product2 = product('burger', 12, 'Veg burger with lettuce and Tomato ')
product3 = product('sandwich', 15, 'Chicken and Salad sandwich' )
product4 = product('wraps', 13, 'Chicken wrap with salad')
menu = [product1, product2, product3, product4]

print("=======Menu=========")

for product in menu:
   print(f"{product.name} - £{product.price:.2f}")

order = []
while True:
  choice = input(f"what would you like to order:  ").lower()

  if choice == 'pizza':
    selected_product = product1
  
  elif choice == 'burger':
   selected_product = product2

  elif choice == 'sandwich':
   selected_product = product3
  
  elif choice == 'wraps':
   selected_product = product4

  else:
   print("sorry! The product is not on the menu")
   continue

  selected_product.display_details()

  quantity = int(input("How many would you like: "))

  order.append({
      'product' : selected_product,
      'quantity': quantity
   })

  another = input("would you like to order another item (yes/no): ").lower()
  if another == 'no':
    break
print("=================")
print("   Your Order")
print("=================")

Total = 0
for item in order:
        product = item["product"]
        quantity = item["quantity"]
        item_Total = product.price * quantity
        #Total = Total + item_total
        Total += item_Total
        print(f"{product.name} * {quantity} = £ {item_Total:.2f}")
print("=====================")
print (f"Total: £{Total:.2f}")

discount = 0

employee = input("Are you an employee (yes/no):  ").lower()

if employee == "yes":
   promo_code = input("enter you promo code: ").upper()
   if promo_code == "SAVE10":
      discount = Total * 0.10
      print("10% discount applied")
   elif promo_code == "SAVE20":
      discount = Total * 0.20
      print("20% discount applied")
   else:
      print("Invalid promo code")
Final_total = Total - discount

print("=============")
print(f"original total: £{Total:.2f}")
print(f"discount: £{discount:.2f}")
print(f"Final total: £{Final_total:.2f}")
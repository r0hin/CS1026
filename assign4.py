from assign4 import *

class Product:
  def __init__(self, name, price, category):
    # Initialize product attributes
    self._name = name
    self._price = price
    self._category = category

  # Define how products are classified
  def __eq__(self, other):
    if isinstance(other, Product):
      if (self._name == other._name and self._price == other._price) and (self._category == other._category):
        return True
    return False

  # Get the name of the product
  def get_name(self):
    return self._name

  # Get the price of the product
  def get_price(self):
    return self._price

  # Get the category of the product
  def get_category(self):
    return self._category

  # Implement string representation
  def __repr__(self):
    rep = ("Product(" + self._name + ", " + str(self._price) + ", " + self._category + ")")
    return rep
  
class Inventory:
  def __init__(self):
    self._inventory = {

    }

  # Add a product to the inventory
  def add_to_productInventory(self, productName, productPrice, productQuantity):
    product = {
      "price": productPrice,
      "quantity": productQuantity
    }
    # Add the product to the inventory
    self._inventory[productName] = product
    pass

  def add_productQuantity(self, productName, addQuantity):
    # Get the product by productName in the inventory
    product = self._inventory[productName]
    # Get the quantity of the product
    quantity = product["quantity"]
    # Add the quantity of the product
    quantity += addQuantity
    # Update the quantity of the product
    product["quantity"] = quantity
    pass

  def remove_productQuantity(self, nameProduct, removeQuantity):
    # Get the product by productName in the inventory
    product = self._inventory[nameProduct]
    # Get the quantity of the product
    quantity = product["quantity"]
    # Remove the quantity of the product
    quantity -= removeQuantity
    # Update the quantity of the product
    product["quantity"] = quantity
    pass

  def get_productPrice(self, nameProduct):
    # Get the product by productName in the inventory
    product = self._inventory[nameProduct]
    # Get the price of the product
    price = product["price"]
    return price

  def get_productQuantity(self, nameProduct):
    # Get the product by productName in the inventory
    product = self._inventory[nameProduct]
    # Get the quantity of the product
    quantity = product["quantity"]
    return quantity

  def display_Inventory(self):
    for key, value in self._inventory.items():
      print(key + ", " + str(value["price"]) + ", " + str(value["quantity"]))

class ShoppingCart:
  def __init__(self, buyerName, inventory):
    self._buyerName = buyerName
    self._inventory = inventory
    self._cart = {}

  def add_to_cart(self, nameProduct, requestedQuantity):
    existingQuantity = self._inventory.get_productQuantity(nameProduct)
    # Check if the quantity of the product in the inventory is greater than or equal to the requested quantity
    if existingQuantity >= requestedQuantity:
      self._inventory.remove_productQuantity(nameProduct, requestedQuantity)
      # Check if the product is already in the cart
      if nameProduct in self._cart:
        self._cart[nameProduct] += requestedQuantity
      else:
        self._cart[nameProduct] = requestedQuantity
      return "Filled the order"
    else:
      return "Can not fill the order"
    
  def remove_from_cart(self, nameProduct, requestedQuantity):
    # Check if the product is in the cart
    if nameProduct in self._cart:
      # Get the existing quantity of the product in the cart
      existingQuantity = self._cart[nameProduct]
      if existingQuantity >= requestedQuantity:
        # Remove the quantity of the product from the cart
        self._cart[nameProduct] -= requestedQuantity
        self._inventory.add_productQuantity(nameProduct, requestedQuantity)
        return "Successful"
      else:
        return "The requested quantity to be removed from cart exceeds what is in the cart"
    else:
      return "Product not in cart"
    
  def view_cart(self):
    # Print the cart
    total = 0
    for key, value in self._cart.items():
      print(key, value)
      # Get the price of the product
      price = self._inventory.get_productPrice(key)
      total += price * value
    print("Total:", total)
    print("Buyer Name:", self._buyerName)

class productCatalog:
  def __init__(self):
    self._catalog = []

  def addProduct(self, product):
    # Check if the product is already in the catalog
    self._catalog.append(product)

  def price_category(self):
    cheap = 0
    expensive = 0
    mid = 0
    for product in self._catalog:
      price = product.get_price()
      if price < 100:
        cheap += 1
      elif price > 499:
        expensive += 1
      else:
        mid += 1

    print("Number of low price items:", cheap)
    print("Number of medium price items:", mid)
    print("Number of high price items:", expensive)

  def display_catalog(self):
    for product in self._catalog:
      # Print the product
      print("Product: " + product.get_name() + " Price: " + str(product.get_price()) + " Category: " + product.get_category())

def populate_inventory(filename):
  inventory = Inventory()

  # Read the file
  with open(filename, "r") as file:
    for line in file:
      line = line.strip()
      line = line.split(",")
      # Add the product to the inventory
      inventory.add_to_productInventory(line[0], int(line[1]), int(line[2]))

  return inventory

def populate_catalog(filename):
  catalog = productCatalog()

  # Read the file
  with open(filename, "r") as file:
    for line in file:
      line = line.strip()
      line = line.split(",") # Split the line by comma
      product = Product(line[0], int(line[1]), line[3])
      catalog.addProduct(product)

  return catalog
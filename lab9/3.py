class CashRegister:
  def __init__(self):
    self._itemCount = 0
    self._totalPrice = 0.0
    
  def addItem(self, price):
    self._itemCount += 1
    self._totalPrice += price

  def clear(self):
    self._itemCount = 0
    self._totalPrice = 0.0

  def getCount(self):
    return self._totalPrice
  
register = CashRegister()
register.addItem(0.90)
register.addItem(0.95)
print(register.getCount())
register.clear()
print(register.getCount())
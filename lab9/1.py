class Car:
  carType = ""
  
  def __init__(self):
    pass

  def setType(self, type):  
    self.carType = type
    pass

  def getType(self):
    return self.carType
    pass

c1 = Car()
c2 = Car()
c3 = Car()

c1.setType("Toyota")
c2.setType("Honda")
c3.setType("Nissan")

print(c1.getType())
print(c2.getType())
print(c3.getType())
temperature = float(input("Temperature of water: "))

state = "liquid"
if (temperature < 0):
  state = "solid"
elif (temperature > 100):
  state = "gas"

print("At {}\u00b0C, water is in the {} state.".format(format(temperature, ".1f"), state))
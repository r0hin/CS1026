class Fan:
    OFF = 0
    ON = 1 
    _state = OFF

    def __init__(self):
        # Initial state
        Fan._state = Fan.OFF

    def turn_on(self):
        Fan._state = Fan.ON

    def turn_off(self):
        Fan._state = Fan.OFF

    def get_stateValue(self):
      state = str(Fan._state)
      if state == "0":
          return "OFF"
      else:
          return "ON"

fan1 = Fan()
fan1.turn_on()
print ("Fan is", fan1.get_stateValue())
fan1.turn_off()
print ("Fan is", fan1.get_stateValue())
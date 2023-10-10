def helloWorld():
  print("Hello World!")

def helloWorldNTimes(n):
  for i in range(n):
    helloWorld()

def main():
  helloWorldNTimes(8)

main()
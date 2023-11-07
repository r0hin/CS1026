filename = input("Enter filename: ")
line = "";
try:
  infile = open(filename, "r")
  line = infile.readline()
except IOError:
  print("File not found")
try:
  value = int(line)
except ValueError:
  print("Invalid integer")
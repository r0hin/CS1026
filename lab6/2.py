text = open("fileone.txt", "r")
myfile = open("filetwo.txt", "w")
line = text.read()
words = line.split()
for word in words:
  print(word)
  myfile.write(word + "\n")

text.close()
myfile.close()
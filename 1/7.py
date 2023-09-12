# Textbox

inputtext = input("Input your text: ")
numdots = inputtext.__len__() + 4
numspaces = inputtext.__len__() + 2

print("*" * numdots)
print("*" + " " * numspaces + "*")
print("* " + inputtext + " *")
print("*" + " " * numspaces + "*")
print("*" * numdots)

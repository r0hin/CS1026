# Textbox

inputtext = input("Input your text: ")
numdots = inputtext.__len__() + 4
numspaces = inputtext.__len__() + 2

print("*" * numdots)
print("*" + " " * numspaces + "*")
print("* " + inputtext + " *")
print("*" + " " * numspaces + "*")
print("*" * numdots)

# template literals example
test = "world";
print(f"Hello {test}");
print("hello %s" % test)
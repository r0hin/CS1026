# Happiness improver

# Sad -> happy, bad -> good, cry -> sing, failed -> passed

inputtext = input("Input your text: ")

inputtext = inputtext.replace("Sad", "Happy")
inputtext = inputtext.replace("sad", "happy")
inputtext = inputtext.replace("Bad", "Good")
inputtext = inputtext.replace("bad", "good")
inputtext = inputtext.replace("Cry", "Sing")
inputtext = inputtext.replace("cry", "sing")
inputtext = inputtext.replace("Failed", "Passed")
inputtext = inputtext.replace("failed", "passed")

print(inputtext)
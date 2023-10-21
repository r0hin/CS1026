def zFirst(words):
# We will need two lists
    zresult = []
    result = []
  
    for word in words:
        if word.lower()[0] == 'z':
            zresult.append(word)
        else:
            result.append(word)
    
        zresult.sort()
        result.sort()
    
    return zresult + result
  
words = ["hello", "good", "nice", "as", "at", "baseball", "absorb", "sword", "a", "tall", "So", "bored", "silver", "hi", "pool", "we", "am", "seven", "do", "you", "want", "ants", "because", "that's", "how", "you", "get", "zebra", "zealot", "zoo", "xylophone", "asparagus"]

print(zFirst(words))


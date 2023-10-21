listInput = ['bgh', 'wer', 'yuy', '1661']
count = 0
for i in listInput:
    if len(i) >= 2 and i[0] == i[-1]:
        count += 1

print(count)

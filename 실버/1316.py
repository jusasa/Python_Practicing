t = int(input())
words = [input() for i in range(t)]
word = []
for i in words:
    spell = []
    for j in range(len(i)):
        if not i[j] in spell and len(i) >= 2:
            spell.append(i[j])
        elif i[j] in spell and i[j] != i[j-1]:
            break
        if j == len(i) - 1:
            word.append(i)
            break
print(len(word))

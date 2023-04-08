t = int(input())
word_list = []
for _ in range(t):
    word = input()
    fake_word = [*word]
    i = 0
    c = 0
    while i + 1 == len(word):
        if fake_word[0] != fake_word[1 + i] and len(word) > 2:
            i += 1
        elif len(word) > 2 and fake_word[0] == fake_word[1 + i]:
            c = 1
            break
    if c == 0:
        word_list.append(word)
    else:
        continue
        
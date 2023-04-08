word = input().lower()
alpha_count = []
alpha = []
for _ in word:
    if not _ in alpha:
        alpha_count.append(word.count(_))
        alpha.append(_)
if alpha_count.count(max(alpha_count)) >= 2:
    print('?')
else:
    print(alpha[alpha_count.index(max(alpha_count))].upper())
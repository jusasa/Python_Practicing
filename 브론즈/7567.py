s = str(input())
d = 10
for i in range(1, len(s)):
    if s[i] != s[i-1]:
        d += 10
    else:
        d += 5
print(d)
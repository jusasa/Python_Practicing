n = int(input())
l = []
for i in range(n):
    a, b, c = map(int, input().split())
    if a == b == c:
        x = 10000 + a * 1000
    elif a == b or a == c or b == c:
        x = 1000 + ((a == b) * a + (a == c) * a + (b == c) * c) * 100
    else:
        x = max([a, b, c]) * 100
    l.append(x)
print(max(l))
a, k = map(int, input().split())
c = 0
for n in range(1, a+1):
    p = int(pow(2, (n // 2) - 1))
    b = n ^ (p-1)
    if n >= b*(pow(2, k)) - 1:
        c += 1
print(c)

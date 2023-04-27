n, m = map(int, input().split())
nu = 2
k = list(range(n, m+1))
while nu * nu <= m:
    for i in range(1, m // (nu * nu) + 1):
        k.remove(i * (nu * nu))
    nu += 1
print(len(k))

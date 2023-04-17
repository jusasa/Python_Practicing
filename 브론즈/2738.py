n, m = map(int, input().split())
a = [input().split() for i in range(n)]
b = [input().split() for j in range(n)]
c = [[0 for k in range(m)] for p in range(n)]
for w in range(n):
    for u in range(m):
        c[w][u] = int(a[w][u]) + int(b[w][u])
for f in c:
    print(*f)
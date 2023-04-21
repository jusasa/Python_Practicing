a = [list(map(int, input().split())) for _ in range(9)]
l = []
j = 0
for j in a:
    l.append(max(*j))
print(max(l))
print(l.index(max(l)) + 1, a[l.index(max(l))].index(max(l)) + 1)

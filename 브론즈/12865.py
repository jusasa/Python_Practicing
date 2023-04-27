l = []
n, k = map(int,input().split())
for i in range(n):
    w, v = map(int, input().split())
    l.append([w, v])
for j in range(n):
    a = [0]
    b = [0]
    if (sum(a) + l[j][0]) <= k:
        a.append(l[j][0])
        b.append(l[j][1])
    else:
        b.remove(l[j][l.index(l[j][min(a)])])
        a.remove(min(a))

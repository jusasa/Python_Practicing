t = int(input())
a = [[0 for i in range(100)] for i in range(100)]
for i in range(t):
    x, y = map(int, input().split())
    for j in range(10):
        for k in range(10):
            a[j+x][k+y] = 1
s = 0
for i in a:
    s += sum(i)
print(s)
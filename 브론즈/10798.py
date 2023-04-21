a = [input().split() for i in range(5)]
for i in range(5):
    a[i][0] = a[i][0].ljust(15, '-')
for j in range(15):
    for i in range(5):
        if not a[i][0][j] == '-':
            print(a[i][0][j], end='')

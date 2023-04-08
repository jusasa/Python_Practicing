a = list(map(int, input().split()))
b = [1,1,2,2,2,8]
for i in range(len(a)):
    if a[i] != b[i]:
        a[i] = b[i] - a[i]
    else:
        a[i] = 0
print(*a)

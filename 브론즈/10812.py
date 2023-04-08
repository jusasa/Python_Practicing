n, m = map(int, input().split())
basket = list(range(1, n+1))
for _ in range(m):
    i, j, k = map(int, input().split())
    basket[i-1:j] = basket[k-1:j] + basket[i-1:k-1]
print(*basket)

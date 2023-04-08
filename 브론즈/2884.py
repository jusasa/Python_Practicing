H,M = map(int,input().split())
m = H*60 + M
if m < 45:
    m = 24*60 + M
m -= 45
print('%d %d' %(m //60,m%60))
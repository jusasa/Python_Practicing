a = int(input())
for i in range(1,a+1):
    print(' '*(a-i)+'*'*(i*2-1))
for j in range(1, a):
    print(' '*j+'*'*(2*a-2*j-1))

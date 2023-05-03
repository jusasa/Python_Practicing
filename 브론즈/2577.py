a = int(input())
b = int(input())
c = int(input())
r = str(a*b*c)
l = []
for i in range(10):
    l.append(r.count(str(i)))
print(*l,sep='\n')
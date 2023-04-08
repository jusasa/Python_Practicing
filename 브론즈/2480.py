a,b,c = map(int,input().split())
l = [a,b,c]
l = sorted(l,reverse=False)
if l[0] == l[1] and l[1]==l[2]:
    l[0] = 10000 +l[0] *1000
    print(l[0])
elif l[0] == l[1] and l[1] != l[2]:
    l[0] = 1000+ l[0]*100
    print(l[0])
elif l[1] == l[2] and l[0]!= l[2]:
    l[1] = 1000+ l[1]*100
    print(l[1])
else:
    l[2]=l[2]*100
    print(l[2])
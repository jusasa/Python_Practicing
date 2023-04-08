l = {'A+': '4.5', 'A0': '4.0', 'B+': '3.5', 'B0': '3.0', 'C+': '2.5', 'C0': '2.0', 'D+': '1.5', 'D0': '1.0', 'F': '0'}
k = 0
m = 0
for i in range(20):
    a, b, c = input().split()
    b = float(b)
    b = int(b)
    c = str(c)
    if not c == 'P':
        for h in l:
            c = c.replace(h, l.get(h))
        c = float(c)
        k += b * c
        m += b
print(k/m)

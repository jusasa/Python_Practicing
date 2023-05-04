s = str(input())
if s[0] == 'A':
    d = 4.0
elif s[0] == 'B':
    d = 3.0
elif s[0] == 'C':
    d = 2.0
elif s[0] == 'D':
    d = 1.0
if s != 'F' and s[1] == '+':
    d += 0.3
elif s != 'F' and s[1] == '-':
    d -= 0.3
if s == 'F':
    d = 0.0
print(d)
t = int(input())
def sus(i):
    return (i*i + i) // 2
for i in range(t):
    s = input()
    su = 0
    suus = 0
    for j in range(len(s)):
        if s[j] == 'O':
           su += 1
        if s[j] == 'X':
            suus += sus(su)
            su = 0
    suus += sus(su)
    print(suus)
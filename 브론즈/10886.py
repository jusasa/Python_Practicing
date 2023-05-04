v = int(input())
s = ''
for i in range(v):
   s = s + str(input())
print("Junhee is cute!" if s.count('1') > s.count('0') else "Junhee is not cute!")
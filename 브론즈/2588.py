F = int(input())
S = int(input())
S1 = S%10
S10 = int((S%100 - S1)/10)
S100 = int((S - S10- S1)/100)
print(F*S1)
print(F*S10)
print(F*S100)
print(F*S)
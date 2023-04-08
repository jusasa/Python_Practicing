c = int(input())
for _ in range(c):
    case = list(map(int, input().split()))
    average =sum(case)/case[0] - 1
    output = 0
    k = 0
    for i in range(case[0]):
        if case[i + 1] > average:
            k += 1
        output = round(k / case[0] * 100, 3)
    print("{:.3f}%".format(output))

while 1:
    a = int(input())
    if a < 0:
        break
    else:
        l = []
        for i in range(1, a + 1):
            if a % i == 0:
                l.append(i)
        l.remove(a)
        if sum(l) == a:
            print(f"{a} = ",end="")
            print(*l,sep=" + ")
        else:
            print(f"{a} is NOT perfect.")
                
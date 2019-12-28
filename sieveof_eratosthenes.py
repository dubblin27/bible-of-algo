def prime123(n):
    notprimelist = []
    primelist = []
    for i in range(2,n+1):
        if i not in notprimelist:
            primelist.append(i)
            for j in range(i*2,n+1,i):
                notprimelist.append(j)
    print(primelist)
c = int(input())
prime123(c)
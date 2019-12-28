def pig(a):
    maxx = max(a)
    minn = min(a)
    size = maxx - minn + 1 
    holes = [0] * size 
    print(holes)
    print(len(holes))
    j = 0
    for i in a :
        while a[j] > 0 :
            if holes[i - minn] != 0 :
                holes.insert(i-minn + 1 , a[j] )
            else : 
                holes [i- minn] = holes[i-minn] +a[j]
            j = j+1 
            break
    for z in holes :
        if z == 0 :
            holes.remove(z)
    print(holes)
    
        


    print(holes)


a = [5,7,3,1,9,3,6]
print(a)
pig(a)

def pigeonhole(a):
    minn = min(a)
    maxx = max(a)
    size = maxx-minn+1
    holes = [0] * size 
    

    for i in a :
        #checks only if integers 
        assert type(i) is int, "integers only please"
        holes[i - minn] += 1 
    
#putting elements in order in the list
    j = 0 
    for c in range(size):
        while holes[c] > 0 :
            holes[c] -= 1 
            
            a[j] = c + minn 
            j = j+1
    print(a)
a = [8, 3, 2, 7, 4, 6, 8] 
pigeonhole(a) 
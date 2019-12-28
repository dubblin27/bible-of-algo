def partialsums(a,x,y):
    
    su = 0
    if x == 0 :
        su = a[y] + sum(a[:y])
    else :
        su = sum(a[:y+1]) - sum(a[:x])
    return su

a = [3,5,6,2,7,1]

x, y = input("Enter a two limits: ").split() 
print(partialsums(a,int(x),int(y)))
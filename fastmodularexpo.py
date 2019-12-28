#recursive
def fastexpo(a,n,mod):
    if n==0 :
        return 1 
    if (n%2 == 0) :
        return (fastexpo((a**2)% mod , n/2 , mod))
    return (a*fastexpo(a,n-1,mod)) % mod 

print(fastexpo(5,13,1000000007))
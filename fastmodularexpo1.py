#iterarive
def fast(a,n,mod):
    ans = 1
    while(n>=1):
        if n%2 == 0 :
            a = (a*a) % mod 
            n = n/2 
        else :
            ans = (ans* a) % mod 
            n=n-1 
    return ans 

print(fast(5,13,1000000007))
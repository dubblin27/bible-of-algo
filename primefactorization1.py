#o(n)
n = int(input("enter a number : "))
i =1 
print("factors are : ")
for i in range(1, n+1 ):
    count = 0 
    if n%i == 0 :
        j =1 
        for j in range(j,i+1) :
            if (i%j == 0) : 
                count = count +1 
        
        if count==2 :
            print(i)

#O(sqrt(n))
import math as ma
n = int(input("enter the prime number to check :"))
j = 1
for i in range(2,int(ma.sqrt(n))-1):
    if n%i == 0:
        j =1
        break
    else :
        j = 0
if j == 0:
    print("prime")
else :
    print("not a")
        
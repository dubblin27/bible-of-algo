su = 0
a = [3,5,6,2,7,1]
print(sum(a))
x, y = input("Enter a two value: ").split() 
x = int(x)
y = int(y)
su = a[y] + sum(a[:y])
print(su)
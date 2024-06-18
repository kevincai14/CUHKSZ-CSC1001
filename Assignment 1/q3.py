m = float(input("Enter a number m:"))
n = 1
while n**2 < m:
    n = n + 1
print("The smallest integer n such that n**2 is greater than m is:" + str(n))

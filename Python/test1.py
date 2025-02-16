# import math


# def isPrime(n) :
#     for i in range(2,int(math.sqrt(n))+1):
#       if (n % i == 0):
#         return False
#     return True
# n=10
# sum=0
# for i in range(1,n+1):
#     if(isPrime(i)):
#         sum+=i
# print("sum = ",sum)

a={1,2,10,5,9,6}
max=0
for i in a:
    if(i>max):
        mmax=max
        max=i
        
print(mmax)
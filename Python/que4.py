# wap to find the missing no in the given list of no.

l1=[1,2,3,5,7,8]
p=l1[0]
i=0
while(i!=len(l1)):
    if(l1[i] != p):
        print(p)
        p+=1
    p+=1
    i+=1

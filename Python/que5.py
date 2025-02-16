
l1=[1,9,2,3,4,26]
# print(l1)
# [1,2,3,4,9,26]
#[1,2,3,4,5,6,7,8,9,10,11,12...,26q]
#[1, 2, 3, 8, 9, 10, 25, 26, 27]
l1.sort()

len=len(l1)
l2=[]
l3=[]

for i in range(0,len-1):
    if l1[i]==l1[i+1]-1:
        l2.append(l1[i])
        l3.append(l1[i])
        print(" ")
    else:
        tem=l1[i]

        
        while(tem!=l1[i+1]-1):
            tem+=1
            l2.append(tem)
        l2.append(tem+1)
        
        
        l3.append(l1[i+1]-1)
        l3.append(l1[i+1])
        l3.append(l1[i+1]+1)

print(l2)
print(l3)
    





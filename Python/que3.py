# wap to find the 3rd a occurance in given alphabets

st="bbsabjcabjkbaic"
o=0
i=0
for var in st:
    if(var=="a"):
        o+=1
        if(o==3):
            print(var.index)
            break
    i+=1

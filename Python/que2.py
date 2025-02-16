a=5
b=4
c=3

if(a+b>c or b+c>a or c+a>b):
    print("This is valid Triangle.\n")
    if((b*b)+(c*c)==(a*a) or (b*b)==(a*a)+(c*c) or (b*b)==(a*a)+(c*c)):
        print("This is Right Angled Triangle.")
    else:
        print("This is not Right Angled Triangle.")


    if(a==b==c):
        print("This is a Equileteral Triangle.")
    elif(a==b or b==c or a==c):
        print("This is Isosceles Triangle.")
    else:
        print("This is Scalene Triangle.")
else:
    print("This is not a valid triangle")


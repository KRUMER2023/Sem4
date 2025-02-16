class Student:
    name=""
    email=""
    def __init__(self,name,email):
        self.name=name
        self.email=email

s1=Student("krunal","xyz")
s2=Student("aditya","abc")

print(s1.name," ",s1.email," ",s2.name," ",s2.email," ")
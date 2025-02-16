class Student:
    name="aman"
    en=2303051240354
    email="wugww"
    list = list()
    print("hello world")
    def __str__(self):
        print(f"name:{self.name}\n email:{self.email}")

s1 = Student()
print(s1.name)
s1.name="patel"
print(s1.name)
print(dir(s1),"\n")
print(dir(list))
s1.__str__()


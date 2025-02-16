# MUltiple Inheritance
class A:
    def speak(self):
        print("class A")

class B:
    def tell(slef):
        print("class B")

class C(A,B):
    def display(slef):
        print("class C")

c1=C()
c1.speak()
c1.tell()


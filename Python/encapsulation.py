class Student:
    def __init__(self,name=None):
        self.__name=name
    def get_name(self):
        return self.__name
    def set_name(self,name):
        self.__name=name
        
st=Student()
st.set_name("krunal")
print(st.get_name())

st1=Student()
st1.set_name("parmar")
print(st1.get_name())
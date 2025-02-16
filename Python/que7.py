# wap to create a lib. class then give some common propeties of lib.
#  create class book , podcasts , magazine , novel
# all 4 inherite the libb. class for using there common properties create individual book , podcasts , magazine , novel
# display data

class Lib:
    title=""
    author=""
    year=0

class Book(Lib):
    nOPage=0
    def __init__(self,title,author,year,nOPage):
        self.title=title
        self.author=author
        self.year=year
        self.nOPage=nOPage
        
    def details(self):
        print("Book Title: ",self.title,"\nBook Author: ",self.author,"\nBook year",self.year,"\nNo. of Page:",self.nOPage,"\n\n")
        

class Podcasts(Lib):
    episode=0
    def __init__(self,title,author,year,episode):
        self.title=title
        self.author=author
        self.year=year
        self.episode=episode
    def details(self):
        print("Podcasts Title: ",self.title,"\nPodcasts Author: ",self.author,"\nPodcasts year",self.year,"\nNo. of Episodes:",self.episode,"\n\n")
        
class Magazine(Book):
    price=0
    def __init__(self,title,author,year,nOPage,price):
        self.title=title
        self.author=author
        self.year=year
        self.nOPage=nOPage
        self.price=price
        
    def details(self):
        print("Magazine Title: ",self.title,"\nMagazine Author: ",self.author,"\nMagazine year",self.year,"\nNo. of Page:",self.nOPage,"\nprice:",self.price,"\n\n")


class Novel(Book):
    def __init__(self,title,author,year,nOPage,price):
        self.title=title
        self.author=author
        self.year=year
        self.nOPage=nOPage
        price=price
        
    def details(self):
        print("Novel Title: ",self.title,"\nNovel Author: ",self.author,"\nNovel year",self.year,"\nNo. of Page:",self.nOPage,"\n\n")

B1=Book("Sea of Theives","Steam",1950,50)
B1.details()

M1=Magazine("Success","MAnish",1990,60,550)
M1.details()

N1=Novel("Road","Rakesh",2000,860,300)
N1.details()

P1=Podcasts("Lazy Talks","SUresh",2024,15)
P1.details()
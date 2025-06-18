class person:
    def __init__(self,name,idno):
        self.name=name
        self.idno=idno
    def display(self):
        print(self.name)    
        print(self.idno)
class employee(person):
    def __init__(self,name,idno,salary,post):
        self.salary=salary
        self.post=post
        person.__init__(self,name,idno)
a=employee("Rahul",5673747,35000,"intern")             
a.display()   
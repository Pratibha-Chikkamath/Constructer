class Student:
    def __int__(self,sno,sname,sub):
        self.sno=sno
        self.sname=sname
        self.sub=sub
    def display(self):
        print(self.sno)
        print(self.sname)
        print(self.sub)
s=Student()
s.sno=1
s.sname="ravi"
s.sub="python"
s.display()

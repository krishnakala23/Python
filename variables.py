class student:
    def __init__(self,name,ro_no):
        self.name=name
        self.ro_no=ro_no
        print("name:",self.name)
        print("ro_no:",self.ro_no)

    def marks(self,marks):
        self.marks=marks
        print("marks:",self.marks)
        
s1=student("raj",150)
s1.marks(90)
s2=student("ram",151)
s2.marks(99)
s3=student("ravi",153)
s3.marks(80)
s4=student("rahul",154)
s4.marks(92)
s5=student("raj",155)
s5.marks(95)


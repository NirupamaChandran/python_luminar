class Student:
    name:str
    roll_no:int
    course:str

    def set_stud(self,name,rollno,course):
        self.name=name
        self.roll_no=rollno
        self.course=course
    
    def display_stud(self):
        print(self.name,self.roll_no,self.course)

stud1=Student()
stud1.set_stud("niru",10,"django")
stud1.display_stud()


stud2=Student()
stud2.set_stud("anu",13,"mearn")
stud2.display_stud()
print(stud2)
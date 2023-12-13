class Employee:
    id:int
    name:str
    dept:str
    salary:int

    def set_emp(self,id,name,dep,sal):
        self.id=id
        self.name=name
        self.dept=dep
        self.salary=sal

    def display_emp(self):
        print(self.id,self.name,self.dept,self.salary)

emp1=Employee()
emp1.set_emp(101,"niru","hr",60000)
emp1.display_emp()

emp2=Employee()
emp2.set_emp(104,"anjitha","qa",50000)
emp2.display_emp()
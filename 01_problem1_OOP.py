#Create a Class "Programmer" for storing information of few programmers working at Microsoft.
class programmer:
    company="Microsoft"
    def __init__(self,name,salary,pin):
        self.name=name
        self.salary=salary
        self.pin=pin
p=programmer("Prithvi",1200000,743166)
print(p.name,p.salary,p.pin,p.company)
r=programmer("Rohan",1200000,743166)
print(r.name,r.salary,r.pin,r.company)

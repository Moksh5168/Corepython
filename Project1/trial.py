class Employee:
    def __init__(self,emp_id,name,email,password,age,salary):
            self.emp_id=emp_id
            self.name=name
            self.email=email
            self.password=password
            self.age=age
            self.salary=salary
        
    def display_employee(self):
          print(f"emp_id : {self.emp_id}, Name :{self.name} , email :{self.email}, password: {self.password}, age :{self.age} , salary :{self.salary} ")
    
class EmployeeDatabase:
        def __init__(self):
            self.employee=[]
        
        def add_employee(self,employee):
              self.employee.list.append(employee)


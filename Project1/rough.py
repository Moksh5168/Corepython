class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def display_employee(self):
        print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}")

class EmployeeDatabase:
    def __init__(self):
        self.employee_list = []

    def add_employee(self, employee):
        self.employee_list.append(employee)

    def remove_employee(self, employee):
        self.employee_list.remove(employee)

    def sort_by_salary(self):
        self.employee_list.sort(key=lambda x: x.salary)

    def display_employees(self):
        for employee in self.employee_list:
            employee.display_employee()

if __name__ == '__main__':
    emp_db = EmployeeDatabase()

    emp1 = Employee("John", 30, 50000)
    emp2 = Employee("Jane", 25, 45000)
    emp3 = Employee("Bob", 28, 55000)

    emp_db.add_employee(emp1)
    emp_db.add_employee(emp2)
    emp_db.add_employee(emp3)

    emp_db.sort_by_salary()

    emp_db.display_employees()

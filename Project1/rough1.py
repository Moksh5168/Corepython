class Employee:
    def __init__(self, emp_id, name, email, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.email = email
        self.age = age
        self.salary = salary

class EmployeeManagementSystem:
    def __init__(self):
        self.employees = []

    def add_employee(self):
        emp_id = input("Enter employee id: ")
        name = input("Enter employee name: ")
        email = input("Enter employee email: ")
        age = int(input("Enter employee age: "))
        salary = int(input("Enter employee salary: "))
        employee = Employee(emp_id, name, email, age, salary)
        self.employees.append(employee)
        print("Employee added successfully!")

    def remove_employee(self):
        emp_id = input("Enter employee id to remove: ")
        for employee in self.employees:
            if employee.emp_id == emp_id:
                self.employees.remove(employee)
                print("Employee removed successfully!")
                return
        print("Employee not found.")

    def view_employees(self):
        for employee in self.employees:
            print(f"ID: {employee.emp_id}, Name: {employee.name}, Email: {employee.email}, Age: {employee.age}, Salary: {employee.salary}")

    def update_employee(self):
        emp_id = input("Enter employee id to update: ")
        for employee in self.employees:
            if employee.emp_id == emp_id:
                employee.name = input("Enter employee name: ")
                employee.email = input("Enter employee email: ")
                employee.age = int(input("Enter employee age: "))
                employee.salary = int(input("Enter employee salary: "))
                print("Employee updated successfully!")
                return
        print("Employee not found.")

# Testing the code
emp_management_system = EmployeeManagementSystem()
while True:
    print("\nEmployee Management System")
    print("1. Add Employee")
    print("2. View Employee")
    print("3. Sort by salary of Employee")
    print("4. Sort by age of Employee")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        emp_management_system.add_employee()
    elif choice == 2:
        emp_management_system.remove_employee()
    elif choice == 3:
        emp_management_system.view_employees()
    elif choice == 4:
        emp_management_system.update_employee()
    elif choice == 5:
        break
    else:
        print("Invalid choice. Please try again.")

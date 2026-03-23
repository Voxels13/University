#Inheritance

class Person:

    def __init__(self,name,age):
        self.name = name
        self.age = age

class Employee(Person):

    def __init__(self,name,age,employee_id,salary):
        super().__init__(name,age)
        self.employee_id = employee_id
        self.salary = salary

class Manager(Employee):

    def __init__(self,name,age,employee_id,salary,department):

        super().__init__(name,age,employee_id,salary)
        self.department = department


    def display(self):
        print(f"Name:{self.name}\nAge:{self.age}\nEmployee_id:{self.employee_id}\nSalary:{self.salary}\nDepartment:{self.department}")

if __name__ == "__main__":

    manager = Manager("John", 36, "192A6", 150000, "Sales")

    manager.display()

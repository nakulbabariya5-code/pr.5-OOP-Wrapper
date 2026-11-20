class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Employee(Person):
    def __init__(self, name, age, emp_id, salary):
        super().__init__(name, age)
        self.__emp_id = emp_id
        self.__salary = salary

    def get_id(self):
        return self.__emp_id

    def set_id(self, emp_id):
        self.__emp_id = emp_id

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary >= 0:
            self.__salary = salary
        else:
            print("Salary cannot be negative")

    def display(self):
        super().display()
        print("Employee ID:", self.__emp_id)
        print("Salary:", self.__salary)


class Manager(Employee):
    def __init__(self, name, age, emp_id, salary, department):
        super().__init__(name, age, emp_id, salary)
        self.department = department

    def display(self):
        super().display()
        print("Department:", self.department)


class Developer(Employee):
    def __init__(self, name, age, emp_id, salary, language):
        super().__init__(name, age, emp_id, salary)
        self.language = language

    def display(self):
        super().display()
        print("Programming Language:", self.language)


person = None
employee = None
manager = None

while True:
    print("\nEmployee Management System")
    print("1. Create Person")
    print("2. Create Employee")
    print("3. Create Manager")
    print("4. Show Details")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        age = int(input("Enter age: "))

        person = Person(name, age)
        print("Person created successfully!")

    elif choice == "2":
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        emp_id = input("Enter employee ID: ")
        salary = float(input("Enter salary: "))

        employee = Employee(name, age, emp_id, salary)
        print("Employee created successfully!")

    elif choice == "3":
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        emp_id = input("Enter employee ID: ")
        salary = float(input("Enter salary: "))
        department = input("Enter department: ")

        manager = Manager(name, age, emp_id, salary, department)
        print("Manager created successfully!")

    elif choice == "4":
        print("\n1. Person")
        print("2. Employee")
        print("3. Manager")

        ch = input("Select details: ")

        if ch == "1":
            if person != None:
                person.display()
            else:
                print("Person not found")

        elif ch == "2":
            if employee != None:
                employee.display()
            else:
                print("Employee not found")

        elif ch == "3":
            if manager != None:
                manager.display()
            else:
                print("Manager not found")

        else:
            print("Wrong choice")

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice")

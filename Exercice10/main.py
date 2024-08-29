class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_details(self):
        print(f"Nom: {self.name}, Âge: {self.age}")


class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def display_details(self):
        super().display_details()
        print(f"Salaire: {self.salary}")

person = Person("Alice", 30)
person.display_details()

employee = Employee("Bob", 40, 50000)
employee.display_details()

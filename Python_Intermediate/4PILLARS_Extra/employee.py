class Employee:
    def __init__(self, name, salary):
        self._name = name
        self.salary = salary

    @property
    def name(self):
        return self._name

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, new_salary):
        if new_salary < 0:
            raise ValueError("El salario no puede ser negativo")
        self._salary = new_salary

    def promote(self, percent):
        self.salary += self.salary * percent


employee = Employee("Ana", 1000)
employee.promote(0.1)

print(employee.salary)

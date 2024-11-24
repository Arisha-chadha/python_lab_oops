class Employee:
    def __init__(self, name, salary):
        self.name = name  
        self._department = None  
        self.__salary = salary 

    def set_department(self, department):  
        self._department = department

    def _set_salary(self, salary): 
        self.__salary = salary

    def __get_salary(self):  
        return self.__salary

    def get_details(self):  
        return f"Name: {self.name}, Department: {self._department}, Salary: {self.__get_salary()}"


emp = Employee("John Doe", 50000)
emp.set_department("IT")  
emp._set_salary(60000)  
print(emp.get_details())  

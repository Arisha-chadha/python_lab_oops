class Student:
    def __init__(self, name, marks):
        self.name = name
        self._marks = marks  

    def update_marks(self, new_marks):
        self._marks = new_marks

    def display(self):
        print(f"{self.name}: {self._marks}")


student = Student("Alice", 85)
student.display()

student.update_marks(90)
student.display()

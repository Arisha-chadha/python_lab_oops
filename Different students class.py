# Define the Student class
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Create objects for different students
student1 = Student("Alice", 20)
student2 = Student("Bob", 22)

# Display information about the students
student1.display_info()
student2.display_info()

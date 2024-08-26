from abc import ABC, abstractmethod 

  

class Student: 

    def __init__(self, id, name, age, major): 

        """ 

        Initialize a Student object. 

  

        Args: 

            id (int): Student ID. 

            name (str): Student name. 

            age (int): Student age. 

            major (str): Student major. 

        """ 

        self.id = id 

        self.name = name 

        self.age = age 

        self.major = major 

  

    def display_student(self): 

        """ 

        Display student information. 

  

        Prints the student's ID, name, age, and major. 

        """ 

        print(f"ID: {self.id}, Name: {self.name}, Age: {self.age}, Major: {self.major}") 

  

class StudentUpdater: 

    @staticmethod 

    def update_student(student, name=None, age=None, major=None): 

        """ 

        Update student information. 

  

        Args: 

            student (Student): The student object to update. 

            name (str, optional): New student name. Defaults to None. 

            age (int, optional): New student age. Defaults to None. 

            major (str, optional): New student major. Defaults to None. 

        """ 

        if name: 

            student.name = name 

        if age: 

            student.age = age 

        if major: 

            student.major = major 

  

class IStudentDatabase(ABC): 

    @abstractmethod 

    def add_student(self, student): 

        """ 

        Abstract method to add a student to the database. 

  

        Args: 

            student (Student): The student object to add. 

        """ 

        pass 

  

    @abstractmethod 

    def remove_student(self, student_id): 

        """ 

        Abstract method to remove a student from the database. 

  

        Args: 

            student_id (int): ID of the student to remove. 

        """ 

        pass 

  

    @abstractmethod 

    def display_all_students(self): 

        """ 

        Abstract method to display all students in the database. 

        """ 

        pass 

  

class StudentDatabase(IStudentDatabase): 

    def __init__(self): 

        self.students = [] 

  

    def add_student(self, student): 

        """ 

        Add a student to the database. 

  

        Args: 

            student (Student): The student object to add. 

        """ 

        self.students.append(student) 

  

    def remove_student(self, student_id): 

        """ 

        Remove a student from the database. 

  

        Args: 

            student_id (int): ID of the student to remove. 

        """ 

        for student in self.students: 

            if student.id == student_id: 

                self.students.remove(student) 

                break 

  

    def display_all_students(self): 

        """ 

        Display information for all students in the database. 

        """ 

        for student in self.students: 

            student.display_student() 

  

# Example usage: 

if __name__ == "__main__": 

    db = StudentDatabase() 

    student1 = Student(1, "Alice", 20, "Computer Science") 

    student2 = Student(2, "Bob", 22, "Mathematics") 

    db.add_student(student1) 

    db.add_student(student2) 

    db.display_all_students() 
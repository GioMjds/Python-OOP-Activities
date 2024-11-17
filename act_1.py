class Student:
    def __init__(self, firstName, lastName, age, studentID, course, block):
        self.fullName = f"{firstName} {lastName}"
        self.age = age
        self.studentID = studentID
        self.course = course
        self.block = block

    def introduce(self):
        print(f"Full Name: {self.fullName}")
        print(f"Age: {self.age}")
        print(f"Student ID: {self.studentID}")
        print(f"Course / Block: {self.course} {self.block}")

student1 = Student("Gio", "Majadas", 21, "231-0165", "BSIT-SD", "2A")
student1.introduce()
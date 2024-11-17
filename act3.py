class GradingSystem:
    def __init__(self):
        self.grades = {
            'prelim': None,
            'midterm': None,
            'final': None
        }

    def getGrade(self, gradeType):
        try:
            grade = float(input(f"Enter your {gradeType} grade: "))
            if 0 <= grade <= 100:
                self.grades[gradeType] = grade
            else:
                raise ValueError("Invalid grade. Value must be between 0 to 100.")
        except ValueError as e:
            print(f"Error : {e}")

    def calculateFinalGrade(self):
        if all(self.grades.values()):
            return sum(self.grades.values()) / 3
        return None

    def getResult(self):
        finalGrade = self.calculateFinalGrade()
        if finalGrade is not None:
            result = "Passed 😊" if finalGrade >= 75 else "Failed 😭"
            print(f"Your final grade is {int(finalGrade)}")
            print(f"You {result}")
        else:
            print("Invalid input")

    def run(self):
        try:
            for gradeType in self.grades:
                self.getGrade(gradeType)
            self.getResult()
        except Exception as e:
            print(f"An error occured: {e}")
        finally:
            print("Goodbye!")

grades = GradingSystem()
grades.run()
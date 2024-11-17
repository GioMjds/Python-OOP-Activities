from act_4_grades import GradingSystem

def main():

    quizScore = float(input("Enter quiz score (raw score): "))
    quizMax = float(input("Enter maximum possible quiz score: "))

    attendanceScore = float(input("Enter attendance score (raw score): "))
    attendanceMax = float(input("Enter maximum possible attendance score: "))

    activityScore = float(input("Enter activity score (raw score): "))
    activityMax = float(input("Enter maximum possible activity score: "))

    examScore = float(input("Enter exam score (raw score): "))
    examMax = float(input("Enter maximum possible exam score: "))

    gradingSystem = GradingSystem(quizScore, quizMax, attendanceScore, attendanceMax, activityScore, activityMax, examScore, examMax)

    finalGrade, result = gradingSystem.getResult()
    
    print(f"Final grade: {finalGrade:.2f}%")
    print(f"Result: {result}")
    
if __name__ == '__main__':
    main()
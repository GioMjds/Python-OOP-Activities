class GradingSystem:
    def __init__(self, quizScore, quizMax, attendanceScore, attendanceMax, activityScore, activityMax, examScore, examMax):
        self.quizScore = quizScore
        self.quizMax = quizMax
        self.attendanceScore = attendanceScore
        self.attendanceMax = attendanceMax
        self.activityScore = activityScore
        self.activityMax = activityMax
        self.examScore = examScore
        self.examMax = examMax

    def calculateFinalGrade(self):
        quiz_weight = 0.20
        attendance_weight = 0.15
        activity_weight = 0.25
        exam_weight = 0.40

        quiz_percent = (self.quizScore / self.quizMax) * 100
        attendance_percent = (self.attendanceScore / self.attendanceMax) * 100
        activity_percent = (self.activityScore / self.activityMax) * 100
        exam_percent = (self.examScore / self.examMax) * 100
        
        final_grade = (quiz_percent * quiz_weight) + (attendance_percent * attendance_weight) + \
                      (activity_percent * activity_weight) + (exam_percent * exam_weight)

        return final_grade

    def getResult(self):
        finalGrade = self.calculateFinalGrade()
        return finalGrade, "Passed 😊" if finalGrade >= 75 else "Failed 😭"
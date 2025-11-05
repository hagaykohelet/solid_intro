from classes.studenta_nd_grade.student import Student,GradeCalculator

if __name__ == "__main__":
    s = Student("hagay",[1,2,3,4,5,6,7,8,9,10])
    g  = GradeCalculator
    g.average_grade(s)
class Student:
    def __init__(self,name:str, grades:list[int]):
        self.name = name
        self.grades = grades



class GradeCalculator:
    @staticmethod
    def average_grade(grades:Student):
        grade = sum(grades.grades)
        sum_grade = grade/ len(grades.grades)
        return sum_grade



# 10-1 교육 내용을 토대로 만든, 학생 정보 저장 클래스


class Student:
    def __init__(self, name, age, grade, major):
        self.name = name
        self.age = age
        self.grade = grade
        self.major = major
        print("인스턴스 초기화 완료")

    def printInfo(self):
        print("이름 : {}/ 나이 : {}/ 학년 : {} / 전공 : {}".format(self.name,
                                                           self.age, self.grade, self.major))


student1 = Student("한영신", 24, 4, "컴퓨터 공학")
student1.printInfo()

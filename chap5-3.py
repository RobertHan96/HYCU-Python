# for문을 이용해 학생들의 점수 분포를 구해서 출력하라
# A : 100~90, B : 89~80, C : 79~70, D : 69~60, F : 59 미만

score = [75, 34, 22, 78, 99, 84, 88, 68, 56, 88, 96,
         47, 67, 83, 91, 95, 77, 73, 78, 81, 83, 71, 70, 13]
grade = [0, 0, 0, 0, 0]
dgree = ["A", "B", "C", "D", "F"]

for point in score:
    if 90 <= point <= 100:
        grade[0] += 1
    elif 80 <= point <= 89:
        grade[1] += 1
    elif 70 <= point <= 79:
        grade[2] += 1
    elif 60 <= point <= 69:
        grade[3] += 1
    else:
        grade[4] += 1

for i in range(0, 5):
    print("Class{} : {}".format(dgree[i], grade[i]))

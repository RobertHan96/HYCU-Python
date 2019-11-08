# 리스트의 값 중 가장 큰값을 구하는 함수 생성하라, 그리고 내장함수 max()와 비교하라
def findMax(num):
    max = 0
    for value in num:
        if value > max:
            max = value
    return max


A = [1, 4, 53, 56, 78, 12, 24, 33, 25, 66]
print(findMax(A))
print(max(A))

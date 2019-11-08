# 두 값 x, y를 받아 x를 y로 나눈 몫과 나머지를 구하라
def clac(x, y):
    return x/y, x % y


mok, nam = clac(10, 3)
# 함수의 결과 값이 2개 이상일 경우 그 결과를 바로 변수에 각각 대입도 가능
print(mok, nam)

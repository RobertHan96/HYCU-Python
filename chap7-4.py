# 재귀 호줄을 이용해 팩토리얼(!)을 구하는 함수 만들기
def fac(num):
    if num == 0 or num == 1:
        return 1
    return num*fac(num-1)


print(fac(2))

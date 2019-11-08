# range() 함수를 이용하여 리스트 [30,29,28, . . .,3,2,1,0]를 생성하고
# 이 리스트의 멤버 3의 인덱스 값은 얼마인지 출력하는 while 문을 작성하라

list = list(range(0, 31))
index = 0
refList = []

while index < len(list):
    if list[index] == 3:
        print("리스트의{}째 값은 {}입니다.".format(index, index))
        break
    else:
        index += 1

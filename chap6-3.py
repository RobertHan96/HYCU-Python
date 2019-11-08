# 셋 컴프리헨션으로 0~20 사이 홀수를 생성하고, 그 중 5번째 값을 출력하라
# 셋 자료형은 num[i] 형태로 인덱싱해서 값을 빼올 수 없음

odd = {num for num in range(20) if num % 2 == 1}
index = 0

for num in odd:
    index += 1
    if index == 5:
        print(index)
        break

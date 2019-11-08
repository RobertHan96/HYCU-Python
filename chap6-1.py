# 리스트 컴플리헨션을 통해 1~20 사이 홀수만 담는 리스트 생성
odd = [num for num in range(0, 21) if num % 2 == 1]
print(odd)

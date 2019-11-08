# 제네러이터와 컴프리헨션을 이용해 0~20사이 홀수를 값 하나씩 출력하라
a = (num for num in range(20) if num % 2 == 1)
for num in a:
    print(num)

'''
1. 튜플 변수 a를 이용하여 튜플 (1,2,3,4,5)를 만들어라.
2. 튜플 변수 a를 이용하여 리스트 [5,4,3,2,1]을 출력하라
'''
a = 1, 2, 3, 4
a = a + (5,)
print(a)

b = list(a + (5,))
b = b.sort(reverse=True)
print(b)

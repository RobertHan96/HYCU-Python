'''
1. a와b를비교하여b에없는요소값을출력하라
2. a와b에모두존재하는요소값을출력하라
3. b에만 있는 요소 값을 출력하라
'''
a = {'young', 'tiger ', 'kahlua', 'old', 'vodka',
     'cream', 'bruss', 'seoul', 'hanyang'}
b = {'tiger', 'dahlua', 'young', 'vodka', 'bruss', 'seoul', 'hanyang'}

print(b-a)
print(a & b)
print(a-b)

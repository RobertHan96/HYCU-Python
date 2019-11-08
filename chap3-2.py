# 아래 리스트 자료형을 하나의 문자열로 바꿔서 출력하라
# Life is too short, you need python.
a = ['life', 'too', 'is', 'short']
b = ['you', 'python', 'need']

a[1], a[2] = a[2], a[1]
a[0] = a[0].capitalize()
print(a)
b[1], b[2] = b[2], b[1]

result = ' '.join(a)+','+' '.join(b)+'.'
print(result)

# 리스트 컴프리헨션 연습

# 표현식을 통해 반복문, 조건문을 적용해서 리스트 바로 생성하기
# 1~10사이 짝수만 담긴 리스트 생성하기
oddList = [odd for odd in range(1, 11) if odd % 2 == 0]
print(oddList)

# 반복문내의 값을 제곱해서 리스트 생성하기
powerList = [num**2 for num in range(1, 6)]
print(powerList)

# 두개의 값을 매개변수로 리스트 생성도 가능함
twoVariable = [(num1, num2) for num1 in range(1, 4) for num2 in range(1, 3)]
print(twoVariable)

# 딕셔너리 컴프리헨션으로 문자열 분리 후 개수 세기
text = "Hello World!"
dic_text = {letter: text.count(letter) for letter in text}
print(dic_text)

# set 함수 사용시 문자열 분리 가능
textSet = set(text)
print(textSet)

# 셋(집합) 컴프리헨션 : 다른 컴프리헨션과 비슷함, 딕셔너리랑 같은 괄호지만 키:밸류 형식이 아님
setA = {num for num in range(1, 11) if num % 3 == 1}
print(setA)

# 튜플은 컴프리헨션이 없고, 제네레이터 컴프리헨션이라고 함
# 일반괄호로 표시하며, 생성 즉시 사용 가능함
a = (num for num in range(0, 5))
for num in a:
    print(num)

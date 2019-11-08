# 문자열의 선언 방법 4가지
a = 'python'
b = "python"
c = """python
hello"""
d = '''python
hello '''
# 따옴표 3개로 감쌀 경우 엔터나 공백이 그대로 반영됨
print(a, b, c, d)

'''
문자열 슬라이싱
    %s : 문자열, %c : 문자 1개, %d : 정수, %f : 실수(부동 소숫점 수)
    %o : 8진수, %x :16진수, %% :% 자체 출력
'''
a = "Life"
print(a[1])  # 특정 문자열 하나
print(a[:])  # 문자열 전체
print(a[1:])  # 특정 문자열 이후 전체, 이전 전체는 반대로 출력 가능
print(a[-1])  # - 인덱싱으로 역순 출력 가능
print(a[::-1])  # 역순으로 전체 출력
print(a[:-1])  # - 인덱싱 하나를 제외한 나머지 출력

# 문자열 포맷팅
#  생략시 오른쪽 정렬 , -를 붙이면 왼쪽 정렬 됨
format1 = "Temparture is %10.2f" % 21.5
print(format1)

# 왼쪽 정렬과 오른쪽 정렬
format1Left = "Temparture is %-10.2f" % 21.5
print(format1Left)

format2 = "humity is %d %%!" % 70
print(format2)

# strip : 공백 제거, (L, R)을 붙여서 좌/우 공백만 제거도 가능함
test1 = ' I  love You  '
test1L = test1.lstrip()
test1R = test1.rstrip()
test1Strip = test1.strip()
print(test1L)
print(test1R)
print(test1Strip)

# replace : 이미 존재하는 내용을 함수에서 지정한 문자열로 교체
print(test1.replace('You', 'DAYE'))

# count : 문자열내 특정 문자의 개수 세기
print(test1.count('o'))

# find : 문자열내에 특정 문자가 있는 첫번째 위치 반환, 없을 경우 -1 반환
print(test1.find('o'))
print(test1.find('z'))
print(test1.index('o'))  # index 함수도 find함수와 같은 기능을함

# JOIN : 문자열에 문자 끼워넣기 빈문자열에 했을때만 쓸모 있을듯
test2 = ''
print(test2.join('DAYE'))

# upper : 대문자로 변환, lower : 소문자 변환, capitalize : 첫글자만 대문자로 변환
print(test1.upper())

''' 
문자열 이스케이프
    \n : 줄 바꿈(개 행), \’ : 단일인용부호, \” :이중인용부호
    \t :수평탭, \r :캐리지 리턴, \f :폼피드, \a : 벨소리, \b : 백 스페이스
    \\ : 문자 \
'''

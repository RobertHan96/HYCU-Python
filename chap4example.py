# 튜플 연습

# 값이 2개씩 짝지어진 텍스트, 리스트, 튜플의 경우 dict() 함수로 딕셔너리 변환 가능
# 텍스트가 3글자 이상이거나, 요소가 3개 이상이면 함수 사용 불가
d_string = 'ab', 'cd', '#A'
print(dict(d_string))
d_list = [['a', '!'], ('tuple1', 'tuple3')]
print(dict(d_list))

testDic = {
    'kim': 1996,
    'han': 1995,
    'hwang': 1965
}
print(testDic)
testDic['han'] = 1996
print(testDic)
testDic['na'] = 1997
print(testDic)
testDic['kim'] = 2002
print(testDic)  # 같은 키값이 두개일 경우 나중에 선언한 값만 살아남음


testDic2 = {
    'hana': 'mura'
}
testDic.update(testDic2)  # update 함수를 통해 앞의 함수에 뒤의 함수 내용 병합 가능
print(testDic)

print(testDic.keys())  # 딕셔너리 전체의 키값 획득 가능
print(list(testDic.values()))  # 딕셔너리 전체의 밸류 획득 가능, 리스트나 튜플로 맵핑도 가능

print(testDic.items())  # items 함수로 키/밸류 모두 출력도 가능

print(testDic.get('hana'))  # 특정 키값을 기준으로 값을 얻을 수도 있음

testDic.pop('hana')  # pop을 특정 밸류 삭제 가능
print(testDic)

# set(집합) : 키값만으로 이루어진 딕셔너리형태, 인덱싱과 중복이 불가능함 순서가 없는 컬렉션
testSet = set()  # 셋은 바로 괄호로 빈 셋을 선언하지 못함,
print(testSet)

# 딕셔너리 처럼 다른 자료형을 셋 자료형으로 만들 수 있다
# 딕셔너리와 달리 값이 쌍으로 이뤄진 경우 셋으로 변환할 수 없다.
testDic3 = ['a', 'c', 'ef', 11]
testSet1 = set(testDic3)
print(testSet1)

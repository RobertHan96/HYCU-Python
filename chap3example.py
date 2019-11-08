# 리스트 활용 예제 연습

# 리스트안에, 리스트 값 생성 후 인덱싱 찾기
a = [[23, 34, "HI"], "TWO", "THREE"]
print(a[0][2])

# 리스트 연산 : 덧셈, 곱셉 가능
b = ["3유", "하루", 300]
print(a+b)
print(b*3)

# 리스트 요소 추가 방법 => append(맨뒤에 추가), insert(원하는 위치에 추가)
b.append(400)
b.insert(0, 1)
print(b)

# extend = 리스트내 요소 병합
a.extend(b)
print(a)

print(a.count(1))  # 리스트내 해당 요소의 개수 세기

# sort : 오름차순 또는 내림차순으로 리스트 요소 정렬 가능, 같은 타입만 있는 리스트에만 사용 가능, 혼합시 불가
# 문자 : 알파벳순 , 숫자 : 오름차순으로 정렬
# reverse = True 옵션을 주면 역순으로 정렬
unsortedList = ["100", "A", "F", "Z", 10, 5, -11]  # 이런 리스트에서는 안됨
unsortedList2 = [10, 5, -11]
unsortedList3 = ["100", "A", "F", "Z"]


# 튜플은 괄호 없이 선언 가능하며, 요소가 1개일 경우에는 반드시 뒤에 ,콤마를 붙여줘야함
# 리스트 대비 적은 메모리 공간만 차지하나, 추후 튜플내 값을 수정할 수 없음
tuple1 = 1, 2, 3
print(tuple1)
tuple2 = 1,
print(tuple2)

# 인덱싱, 덧셈, 곱셈 등의 연산 방법은 리스트와 튜플 모두 동일함

# 튜플을 이용한 변수 할당 : 변수 개수만 큼 튜플의 인덱스 값이 배치됨
a, b, c = (["kim", "park", "han"], "name", "age")
print(a, b, c)

# 튜플의 값 교환 : 임시 변수 없이 상호 호출로 바로 가능
tuple3 = 3,
tuple4 = 4,
tuple3, tuple4 = tuple4, tuple3
print(tuple3, tuple4)
tuplesum = tuple3 + tuple4
print(tuplesum)

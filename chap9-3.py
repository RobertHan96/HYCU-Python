# 리스트 변수 names에 있는 각 요소들의 마지막 문자를 기준으로 오름차순 정렬을 하여 출력하고자 한다.
# sorted() 함수의 key 파라미터에 익명 함수를 사용하여 작성하라.
# names = [‘Kim’, ‘Jeong’, ‘Park’, ’Lee’, ’Choi’]

names = ['kim', 'choi', 'park', 'lee', 'jeong']
print(sorted(names, key=lambda name: name[-1]))

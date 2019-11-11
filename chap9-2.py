# 다음 리스트 변수 list_name의 각 항목을 출력시키는 제너레이터 my_names를 정의하라.
# 단, 출력되는 각 항목의 첫 글자는 대문자가 되도록 하라.

# list_name = [‘kim’, ‘choi’, ‘park’, ‘jeong’, ‘lee’]
import sys
list_name = ['kim', 'choi', 'park', 'jeong', 'lee']


def capNames(list):
    for name in list:
        yield name.cap

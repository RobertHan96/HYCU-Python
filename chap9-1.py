# range() 함수와 같은 동작을 하는 제너레이터 함수 my_range()를 정의하라.


def my_range(first, last, step):
    num = first
    while first < last:
        yield num
        num += step


print(type(my_range))
myFunc = my_range(1, 10, 2)
print(type(myFunc))

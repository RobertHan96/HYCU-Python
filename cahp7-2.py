# N개의 숫자를 입력받아 평균을 구하는 함수 만들기, *인자 사용
def avg(*args):
    total = 0
    for total in args:
        total += total
    print(total//len(args))


avg(5, 5)

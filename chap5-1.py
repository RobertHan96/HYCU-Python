# 2단~9단을 출력하는 프로그램 만들기
for x in range(2, 10):
    print('\n')
    for y in range(1, 10):
        print("{}x{} = {}".format(x, y, x*y), end=" ")

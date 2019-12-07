# 1) Negative Power Error 예외클래스를 정의하라
# 2) a, b를 입력 인자로 받아 a**b를 반환하는 PositivePower 함수를 정의하라
# 3) b < 0 이면 Negative Power Error 예외를 발생시키고, 메시지를 출력하라

class NegativePowerError(Exception):
    pass
def PositivePower(a, b) : 
    if b  < 0 :
        try : 
            raise NegativePowerError
        except NegativePowerError : 
            print("두번째 입력 값이 음수입니다.")
    return a**b

print(PositivePower(3, -2))
print(PositivePower(3, 2))
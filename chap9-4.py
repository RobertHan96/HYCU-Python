# 다음 두 함수에 대해 ‘Hi, python!’과 ‘Bye, python!’이 출력되도록 데코레이터 함수를 정의하여 실행하라.
# >>>def hi_python(): return ‘Hi, ‘
# >>>def bye_python(): return ‘Bye, ‘


def hi_python():
    return 'Hi,'


def bye_python():
    return 'Bye,'


def python(func):
    def newString(*args, **kwargs):
        print(func(), 'python!')
    return newString

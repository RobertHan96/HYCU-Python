# 함수 연습


def nickname(nickname1, nickname2, nickname3):
    return {'nickname1': nickname1, 'nickname2': nickname2, 'nickname3': nickname3}


# 함수의 키워드 인자 : 함수에서 정의한 이름에 = 연산자를 통해 값 대입, 입력인자의 순서를 몰라도되므로 편리
# 순서를 바꿔 써도, 값을 알아서 찾아가므로 더 편리
print(nickname(nickname1="만보", nickname2="멋쟁이", nickname3="보바"))

# 함수의 위치 인자 : 함수를 정의할때 쓴 입력인자 순서대로 값을 그냥 쓰기만하면됨, 순서 기억 필요
print(nickname("만보", "보바", "왕자"))

# 인자의 복합 사용 : 키워드 인자, 위치 인자 혼합해서 사용 가능하나,
# 위치 인자를 먼저 쓰고, 키워드 인자를 나중에 써야만 함수 호출이 가능함, 아니면 에러 발생
print(nickname("만보", nickname3="보바", nickname2="멋쟁이"))
# 아래처럼 쓰면 안됨, argument에러 발생
# print(nickname(nickname3="보바", "하나무라", nickname2="멋쟁이"))


# *로 함수의 입력인자를 튜플로 모으기 : 입력 인자 개수가 정해지지 않았을때 유용
def sum(*values):
    sum = 0
    for num in values:
        sum += num
    return sum


print(sum(13, 28, 33))

# 위치인자, *인자 혼합사용시 : 위치인자가 앞에 와야 함


def fam_name(familyname, *names):
    for name in names:
        print("{}  {}".format(familyname, name))


fam_name('HAN', 'YONGSHIN', 'HANA', 'SUCKBONG')

# **인자 : 인자의 이름, 개수도 정해지지 않았을 경우 추후 정의해서 사용 가능


def kboTeams(**temas):
    team = temas.keys  # 함수의 키(인자) 값으로 선언
    for team in temas:
        print(team, ':', temas[team])


kboTeams(KIA='Tigers', DOSAN='Bears', SK='Wibunse')
# 각 인자를 모두 혼합해서 쓰려고 할 경우, 아래 순서대로 써야 사용 가능함
# 위치인자 => 키워드 인자 => *인자 => **인자

# 함수 생성시 인자의 기본값을 생성해서 할당할 수 도 있음
# 함수의 기본값은 함수 선언시 맨 마지막에 써줘야함


def fam_name2(*names, familyname="HAN"):
    for name in names:
        print("{}  {}".format(familyname, name))


fam_name2('YONGSHIN', 'HANA', 'SUCKBONG')

# 기본값을 지정하더라도 함수 사용시 기본값을 바꾸면, 나중 값으로 변경됨
fam_name2('YONGSHIN', 'HANA', 'SUCKBONG', familyname="KIM")

# 가족의 성씨를 입력받고, 가족의 이름을 입력 받은 후 차례대로 출력하는 클래스를 생성하라

class Family_name : 
    def __init__(self, family_name) : 
        self.family_name = family_name
        print("init 함수가 실행되었습니다.")
        print(id(self))
    
    def set_name(self, *args): 
        self.names = args

    def pnr_names(self) :
        for name in self.names : 
            print(self.family_name, name)

myFamily = Family_name("Han")
myFamily.set_name("YONG SHIN", "SUNG YONG", "JIN SIM")
myFamily.pnr_names()

temp_id = Family_name("Han")
print(id(temp_id))


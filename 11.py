# 부모 클래스 Calc를 상속 받는 자식 클래스 Average를 작성하라
# 1) Calc의 인자의 값의 합과 개수를 반환하는 메소드를 작성하라
# 2) Calc를 이용하여 입력 입자값들의 평균을 구하는 인스턴스 메소드를 클래스 Average내에 작성하라

class Claculator():
    def __init__(self, a, b, c) : 
        self.data = [a,b,c]
    def sumInput(self):
        return sum(self.data)
    def countInput(self) : 
        return len(self.data)

class Average(Claculator):
    def inputAverage(self) : 
        return self.sumInput()/self.countInput()

a = Average(1,4,6)
print(a.__dict__)
print(a.inputAverage)

# 위에 작성한 Average 클래서에 입력개수를 제한하지 않도록 오버라이딩해서 재작성하라.
class NewAverage(Claculator):
    def __init__(self, *arg) :
        self.data = arg
    def inputAverage(self) : 
        return self.sumInput()/self.countInput()
a = NewAverage(2,4,6,8,10,12,14)
print(a.inputAverage, a.__dict__)
# 아래 리스트의 각 요소 첫글자를 대문자로 바꾸고, 주말과 주중을 구분해서 두개의 리스트를 생성하라
days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
days[0] = days[0].capitalize()
days[1] = days[1].capitalize()
days[2] = days[2].capitalize()
days[3] = days[3].capitalize()
days[4] = days[4].capitalize()
days[5] = days[5].capitalize()
days[6] = days[6].capitalize()

weekdays = days[:5]
weekends = days[5:]

print(weekdays)
print(weekends)

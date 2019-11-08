'''
1. ‘minsoo’의 출생 년도가 잘못되어 있다. 1994로 바꿔라 
2. 마지막 요소 ‘jaesup’:2002 를 삭제하라
3. names의 모든 요소들을 지워 빈 딕셔너리로 만들어라
'''
names = {'cholsoo': 1962, 'younghee': 1965, 'minsoo': 1894, 'jaesup': 2002}
names['minsoo'] = 1994
names.pop('jaesup')
print(names)
names = names.clear()
print(names)

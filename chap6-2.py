# 딕셔너리 컴프리헨션으로 {"a" : 97}과 같이 알파벳 : 아스키코드 값을 쌍으로 딕셔너리를 생성하라

char = 'abcdefghijklmnopqrstuvwxyz'
charDic = {letter: char.index(letter)+97 for letter in char}
print(charDic)

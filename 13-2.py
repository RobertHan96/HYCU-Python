# pythonlife 내용을 텍스트파일 hipython.text에 작성하라
f=open('F:\\HYCU\\2019 2학기\\파이썬기반 코딩교육\\hipython.text', 'xt')
pythonfile = '''
Life is too short
You need Python!
'''
for char in pythonfile :
    f.write(char)
f.close()


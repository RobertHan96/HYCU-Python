# 13-2.py의 hipython.txt에 문장을 추가하라 
# 단 with-open-as 문을 사용하여 close를 사용하지 않아야 함

with open('F:\\HYCU\\2019 2학기\\파이썬기반 코딩교육\\hipython.text', 'a') as f:
    f.write(''' Happy Python!''')
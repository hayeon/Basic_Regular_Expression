import re
import sys

while True:
    str = sys.stdin.readline().rstrip('\n')
    if not str:
        break

    s = len(re.findall('[a-z]', str)) #소문자 찾기
    l = len(re.findall('[A-Z]', str)) #대문자 찾기
    n = len(re.findall('[0-9]', str)) #숫자 찾기
    b = len(re.findall(' ', str)) #공백찾기

    print(s, l, n, b) #출력

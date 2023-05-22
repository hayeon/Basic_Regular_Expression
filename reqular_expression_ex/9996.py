import re
import sys


input = sys.stdin.readline
n = int(input())  # 반복 횟수 입력

s, e = input().rstrip().split("*")  # 정규식을 입력받은 후, 한글자씩 분리
re = re.compile(s+".*"+e+"+")  # 정규식 컴파일

for i in range(n):  # n번 반복
    str = input().rstrip() #문자열 입력
    a = re.search(str) #search() 메소드를 이용하여 str과 정규식 비교
    if a and a.group() == str: #a가 존재하고, a.group()과 str이 같다면
        print("DA")       #DA 출력
    else:
        print("NE")     #NE 출력

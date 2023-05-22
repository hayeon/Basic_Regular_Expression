import re  # 모듈 포함하기

a = input()  # 문서
b = input()  # 검색어

p = re.compile(b)  # 검색어를 조건으로 가짐
m = p.findall(a)  # findall()을 사용하여 패턴과 매치되는 모든 값을 찾아 리스트로 리턴, 검색어에 해당하는 것 찾기

print(len(m))  # 리스트 갯수 출력

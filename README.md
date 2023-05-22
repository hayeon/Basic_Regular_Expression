# Python에서의 Regular Expression과 Garbage Collection

## Regular Expression 

1. [정규 표현식(Regular Expressions)의 개념](#정규-표현식regular-expressions의-개념)

2. [정규 표현식(Regular Expressions)은 왜 필요한가?](#정규-표현식regular-expressions은-왜-필요한가)

3. [정규 표현식(Regular Expressions)의 기본 문법](#정규-표현식regular-expressions의-기본-문법)

    - [메타문자(meta characters)의 종류](#메타문자meta-characters의-종류)
        -  문자클래스[ ]
        -  Dot(.)        
        -  반복(*)
        -  반복(+)
        -  반복({m,n}, ?)
    - [re 모듈](#re-모듈)
    - [문자열 검색 Method](#문자열-검색-method)    
        -  match
        -  search        
        -  findall
        -  finditer   
    - [백 슬래시 \\](#백슬래시-b)
4. [정규식 예제 문제](#예제문제)

## Regular Expression 

<br/>
<br/>
<br/>

---
## 정규 표현식(Regular Expressions)의 개념

<br/>

> (1)<B> 정규 표현식(Regular Expressions)</B>은 복잡한 문자열을 처리할 때 사용하는 기법으로, 문자열을 처리하는 모든 언어에서 사용합니다. <p> (2) 문자열에서 원하는 패턴을 찾거나, 대체하거나, 추출하는 등의 다양한 문자열 처리 작업을 수행할 수 있습니다. <p>(3) 줄여서 <B>"정규식"</B>이라고도 말합니다.

<br/>


---
## 정규 표현식(Regular Expressions)은 왜 필요한가?
<br/>

>정규식을 사용하면 훨씬 간편하고 직관적인 코드를 작성할 수 있습니다.

<br/>

### <b>ex) 정규식 없이 전화번호 가운데를 *로 바꾸기
```python
data = """
yang 010-1234-5678
kim 010-7777-8888
"""

result = []
for line in data.split("\n"): #한글자씩 자르기
    word_result = []
    
    for word in line.split(" "):
#단어의 길이가 13이고, 처음 3글자가 숫자이며, 나머지 부분도 숫자인 경우
        if len(word) == 13 and word[:3].isdigit() and word[4:].isdigit(): 
            word = word[:6] + "-" + "*" * 4 + "-" + word[11:]
        word_result.append(word)
    
    result.append(" ".join(word_result))

print("\n".join(result))
```
>결과값

```
yang 010-****-5678
kim 010-****-8888
```
<br/>
<br/>


### <b>ex) 정규식을 사용하여 수정된 코드

```python
import re

data = """
yang 010-1234-5678
kim 010-7777-8888
"""

pattern = r"(\d{3})-(\d{4})-(\d{4})"
replacement = r"\1-****-\2"

result = re.sub(pattern, replacement, data)

print(result)
```

>결과값

```
yang 010-****-5678
kim 010-****-8888
```
이처럼 정규표현식을 사용하면, 길었던 코드를 간결하고 클린하게 적용할 수 있습니다.

<br/>
<br/>

---
## 정규 표현식(Regular Expressions)의 기본 문법
<br/>
<br/>
<br/>

## 메타문자(meta characters)의 종류
> 메타문자란? 특별한 용도로 사용하는 문자를 말합니다.

```python
# 사용되는 메타 문자의 예시
. ^ $ * + ? { } [ ] \ | ( )
```
<br/>
<br/>


## <b> 1. 문자 클래스 [ ]
> [ ] 사이에는 어떤 문자도 들어갈 수 있습니다. 

<br/>

## 문자열 "a", "before", "dude"가 정규식 [abc]은 어떻게 매치될까?
<br/>


* "a"는 정규식과 일치하는 문자인 "a"가 있으므로 매치
* "before"는 정규식과 일치하는 문자인 "b"가 있으므로 매치
* "dude"는 a, b, c 중 어느 하나도 포함하고 있지 않으므로 매치되지 않음

<br/>


## 하이픈(-)을 사용한 문자 클래스의 사용 예시
<br/>

> [ ] 안에 하이픈(-)을 사용하면 두 문자 사이의 범위(From - To)를 의미한다. 예를 들어, [a-c]라는 정규 표현식은 [abc]와 동일하고 [0-5]는 [012345]와 동일합니다.

* [a-zA-Z] : 알파벳 소문자 대문자 모두
* [0-9] : 숫자

 > ⭐ [ ] 안에 ^를 사용할 경우, <b>not</b>의 의미를 갖습니다. <br/> [^0-9]은 <b> 숫자가 아닌, 문자만 매치됩니다.</b>

<br/>

## 자주 사용하는 문자 클래스

>대문자로 표기 될 경우, NOT의 의미를 지닙니다.

|표기법|내용|동일 표현식|
|------|---|---|
|\d|숫자와 매치|[0-9]|
|\D|숫자가 아닌 것과 매치| [^0-9]|
|\s|whitespace 문자와 매치|[   \t\n\r\f\v]
|\S|whitespace 문자가 아닌 것과 매치| [^ \t\n\r\f\v]
|\w |문자+숫자와 매치| [a-zA-Z0-9_]
|\W |문자+숫자가 아닌 문자와 매치|  [^a-zA-Z0-9_]

<br/>
<br/>
<br/>
<br/>

---

## <b>2. Dot(.)
> 줄바꿈 문자인 \n을 제외한 모든 문자와 매치됨을 의미합니다.

```python
# a + 모든문자 + b 
# => 즉, a와 b 사이에 어떤 문자가 들어가도 모두 매치된다는 의미
a.b

# a + 모든문자 + b를 만족함으로, 정규식과 매치된다.
"aab" 

#a + 모든문자 + b를 만족함으로,정규식과 매치된다.
"a0b"

# "a"와 "b"사이에 어떤 문자라도 있어야 하는 a.b 일치하지 않으므로, 매치되지 않는다.
"abc"
```



### <b>a[.]b</b> 
<br/>
이 정규식의 의미는 다음과 같습니다.

> "a + (.)문자 + b"

### <b>따라서, 정규식 a[.]b는 "a.b" 문자열과 매치되고, "a0b" 문자열과는 매치되지 않는다.</b>
<br/>

+ 문자 클래스[] 내에 (.) 메타 문자가 사용된다면 "모든 문자"라는 의미가 아닌 문자 . 그대로를 의미합니다

<br/>
<br/>
<br/>
<br/>

---

## <b>3. 반복

<br/>

## *을 사용한 반복 매치
> (*) 앞에 문자가 0번 이상 반복될 시, 매치된다. <em>즉, 해당 문자가 없어도 매치가 된다 </em>
```python
ca*t    # 정규식

ct      # "a"가 0번 반복되어 매치
cat     # "a"가 0번 이상 반복되어 매치 (1번 반복)
caaat   # "a"가 0번 이상 반복되어 매치 (3번 반복)

```

<br/>

## +을 사용한 반복 매치
> (+) 앞에 문자가 1번 이상 반복될 시, 매치됩니다. <em>즉, 해당 문자가 1번 이상 반복되어야합니다.. </em>
```python
ca+t    # 정규식

ct      # "a"가 0번 반복되어 매치 X
cat     # "a"가 1번 이상 반복되어 매치 (1번 반복)
caaat   # "a"가 1번 이상 반복되어 매치 (3번 반복)

```
<br/>

## 반복 횟수 제한하기  {m,n}

<br/>

> {m, n} 정규식을 사용하면 반복 횟수가 m부터 n까지 매치할 수 있습니다. 또한 m 또는 n을 생략할 수도 있습니다. 만약 {3,}처럼 사용하면, 반복 횟수가 3 이상인 경우이고 {,3}처럼 사용하면 반복 횟수가 3 이하를 의미합니다. 생략된 m은 0과 동일하며, 생략된 n은 무한대의 의미를 갖습니다.

<br/>

```python
ca{2}t    # 정규식: c + a(2회 반복) + t
#문자열
cat       # "a"가 1번만 반복되어 매치되지 않음
caat      # "a"가 2번 반복되어 매치

# --------------------------

ca{2,5}t    # 정규식: c + a(2-5회 반복) + t
#문자열
cat         # "a"가 1번만 반복되어 매치되지 않음
caat        # "a"가 2번 반복되어 매치
caaaaat     # "a"가 5번 반복되어 매치
caaaaaaat   # "a"가 7번 반복되어 매치되지 않음
```

<br/>

## ?
>? 메타문자가 의미하는 것은 {0, 1}를 의미합니다. 
즉, ? 앞에 문자가 있어도 되고, 없어도 된다는 의미가 됩니다. 

```python
ab?c    # "a + b(있어도 되고 없어도 된다) + c
#문자열
abc     #b가 1번 사용되어 매치
ac      #b가 0번 사용되어 매치
```


---

<br/>
<br/>

## <b> re 모듈</b>
> python은 re(regular expression) 모듈을 제공합니다. re 모듈은 파이썬을 설치할 때 자동으로 설치되는 표준 라이브러리, import하여 사용됩니다. 
```python
 import re
 p = re.compile('ab*') # re.compile을 사용하여 정규식을 컴파일한다.   그 이후의 작업은 객체 p를 사용하여 수행된다.
```


<br/>
<br/>

---

## <b> 문자열 검색 Method </b>

<br/>

|Method|기능|
|------|---|
|match()|문자열의 처음부터 정규식과 매치되는지 조사한다.|
|search()|문자열 전체를 검색하여 정규식과 매치되는지 조사한다.|
|findall()|정규식과 매치되는 모든 문자열(substring)을 리스트로 리턴한다.|
|finditer()|정규식과 매치되는 모든 문자열(substring)을 반복 가능한 객체로 리턴한다.

<br/>
<br/>

## <b> (1) match() </b>
<br/>

### 예제 1
```python
 import re
 p = re.compile('ab*') #이 때 p는 "패턴객체"라고 한다.

m = p.match("python")
print(m)


#결과: [a-z]+ 정규식에 부합되므로 match 객체를 돌려준다.
<re.Match object; span=(0, 6), match='python'>
```

### 예제 2

```python
 m = p.match("3 python")
print(m)


#결과: 문자 3이 정규식 [a-z]+에 부합되지 않으므로 None을 돌려준다.
None
```
<br/>
<br/>

## 따라서, match의 흐름도는 다음과 같습니다.

```python
import re
p = re.compile(정규표현식)
m = p.match('string goes here')
if m:
    print('Match found: ', m.group())
else:
    print('No match')

```

<b> match의 결괏값이 있을 때만 그다음 작업을 수행하는 로직을 구성할 수 있습니다.</b>

<br/>
<br/>

##  <b> (2) search() </b>

<br/>

> search()는 match()와 달리 문자열 전체를 검색합니다.

<br/>

```python
m = p.search("python")
print(m)

# 결과 : match 메서드를 수행했을 때와 동일하게 매치된다.
<re.Match object; span=(0, 6), match='python'>
```

```python
m = p.search("3 python")
print(m)

# 결과 : search는  문자열 전체를 검색하기 때문에 "3 " 이후의 "python" 문자열과 매치된다.
<re.Match object; span=(2, 8), match='python'>
```

<br/>
<br/>

##  <b> (3) findall() </b>

<br/>

> 패턴과 매치되는 모든 값을 찾아 리스트로 리턴합니다.

<br/>

```python
result = p.findall("life is too short")
print(result)

# 결과 : 패턴([a-z]+)과 매치되는 모든 값을 찾아 리스트로 리턴한다.
['life', 'is', 'too', 'short']
```
<br/>
<br/>

##  <b> (4) finditer() </b>

```python
result = p.finditer("life is too short")
print(result)
#결과
<callable_iterator object at 0x01F5E390>


for r in result: print(r)
... 
#결과
<re.Match object; span=(0, 4), match='life'>
<re.Match object; span=(5, 7), match='is'>
<re.Match object; span=(8, 11), match='too'>
<re.Match object; span=(12, 17), match='short'>
```

>findall과 동일하지만, 그 결과로 반복 가능한 객체를 리턴합니다. <p> 반복 가능한 객체가 포함하는 각각의 요소는 match 객체입니다.

<br/>
<br/>
<br/>
<br/>

---
##  <b> match 객체의 메서드</b>

<br/>

>  match()와 search()를 수행한 결과로 리턴된 match 객체를 통해 어떤 문자열이 매치되었지, 매치된 문자열의 인덱스는 어디서부터 어디까지인지를 알 수 있습니다.

<br/>

|Method|기능|
|------|---|
|group()|매치된 문자열을 리턴한다.|
|start()|매치된 문자열의 시작 위치를 리턴한다.|
|end()|매치된 문자열의 끝 위치를 리턴한다.|
|span()|매치된 문자열의 (시작, 끝)에 해당하는 튜플을 리턴한다.|

<br/>

예제 1 - match
```python
>>> m = p.match("python")

>>> m.group()
'python'

>>> m.start()
0 #시작 위치는 0

>>> m.end()
6 #끝 위치는 6

>>> m.span()
(0, 6)

```

예제 2 - search
```python
>>> m = p.search("3 python")

>>> m.group()
'python'

>>> m.start() #python은 2번째부터 위치함
2

>>> m.end() #python은 8번째에서 끝남
8

>>> m.span()
(2, 8)

```

<br/>

---
##  <b>re 모듈을 사용하여 축약하기 </b>
```python
#기존코드
>>> p = re.compile('[a-z]+')
>>> m = p.match("python")


#re 모듈을 사용하여 축약한 코드
>>> m = re.match('[a-z]+', "python")


```
>위처럼 컴파일과 match 메서드를 한 번에 수행할 수 있습니다. <p>한 번 만든 패턴 객체를 여러번 사용해야 할 때, 이 방법보다 re.compile을 사용하는 것이 편리합니다. 

<br/>
<br/>
<br/>

---

## <b>백슬래시 \</b>

<br/>
<br/>

### (1) 파이썬의 백슬래시에서 겪는 문제
```
\section
```
<br/>

위의 정규식은 \s 문자가 whitespace로 해석되어 의도한 대로 매치가 이루어지지 않습니다.
<p> 따라서, 우리는 다음과 같이 변경해야 합니다.

```
\\section
```

 문자가 문자열 자체임을 알려 주기 위해, 백슬래시 2개를 사용하여 이스케이프 처리를 합니다.
따라서 위 정규식을 컴파일하려면 다음과 같이 작성해야합니다.


```python
>>> p = re.compile('\\section')
```

### 그러나, 실제로 컴파일하면 파이썬 문자열 리터럴 규칙에 따라 <b>\\이 \ </b> 로 변경되어 \section이 전달됩니다. <p> <em>결국 정규식 엔진에 \\ 문자를 전달하기 위해 파이썬은 \\\\ 백슬래시를 4개를 사용해야합니다. </em>

<br/>

```python
>>> p = re.compile('\\\\section')
```
<br/>

### 이러한 문제를 해결하기 위해  Raw String을 사용합니다.

```python
>>> p = re.compile(r'\\section')
```


> ### 정규식 문자열 앞에 r 문자를 삽입하면 이 정규식은 Raw String 규칙에 의해, 백슬래시 2개 대신 1개만 써도 2개를 쓴 것과 동일한 의미를 갖게 됩니다. <p>
### <em> + 만약 백슬래시를 사용하지 않는 정규식이라면, r의 유무에 상관없이 동일한 정규식이 됩니다. </em>
<br/>
<br/>

---
<br/>

## <b>예제문제</b>

<br/>

> ### 정규식의 예제문제는 백준의 예제 문제를 사용했습니다. 풀이와 문제는 해당 파일을 참고해주세요.

<br/>
<br/>

---
<br/>

참고 자료<p>
[점프투파이썬](https://wikidocs.net/1642) <p>
백준
* [문서검색](https://wikidocs.net/1642)
* [한국이 그리울 땐 서버에 접속하지](https://www.acmicpc.net/problem/9996)
* [문자열 분석](https://www.acmicpc.net/problem/10820)


"""
2025.03.18 화
"""

print()
print()
print("------------------------")
print("--- 문자열 인덱스 복습")
print("------------------------")
print()

# 예제 1
s = "hello"

# 'h'를 출력하고 싶을 때
first_char = s[0]
print(first_char)

# (역순) O를 출력하고 싶을 때
last_char = s[-1]
print(last_char)

# 'l'을 출력하고 싶을 때
third_char = s[2]
print(third_char)
print(s[-3])

print()
print()
print("------------------------")
print("--- 문자열 슬라이싱")
print("------------------------")
print()

'''
[문자열 슬라이싱]

- 문자열의 일부를 원하는 만틈 잘라내는 기능

[문법]

- 문자 열을 담은 변수명 [start : stop : step]
- start(시작 인덱스): 슬라이싱을 시작할 위치를 지정. 생략 가능. 기본 값은 0
- stop(종료 인덱스): 슬라이싱을 종료할 위치를 지정. 생략 가능. 기본 값은 (마지막 인덱스+1)
- step(증감폭): 인덱스의 증가 또는 감소 값을 지정. 생략 가능. 기본 값은 1씩 증감.
'''

# 예제 1
text = "I Love Python"

# Love
substring01 = text[2:6]
print(substring01)

# Python = text[7:13]
substring02 = text[-6:]
print(substring02)

# Pto = text[7:13:2]
substring03 = text[7:-1:2]
print(substring03)

# Lv
substring04 = text[2:6:2]
print(substring04)

print()
print("------------------------")
print()

# 예제 2
text01 = "I Absolutely Love Python Programming"

# Absolutely
substring05 = text01[2:12]
print(substring05)

# Love
substring06 = text01[13:17]
print(substring06)

# Asltl
substring07 = text01[2:12:2]
print(substring07)

print()
print()
print("------------------------")
print("--- 문자열 길이")
print("------------------------")
print()

'''
[문자열 길이]

- len() 함수 사용
- 문자열의 길이는 공백을 포함한 모든 문자의 개수
'''

# 예제 1
text03 = "Python"
text03_length = len(text03)
print(text03_length)

print()
print("------------------------")
print()

# 예제 2
text04 = "I Love Python"
text04_length = len(text04)
print(text04_length)

print()
print()
print("----------------------------")
print("--- 소문자 ↔ 대문자 변환")
print("----------------------------")
print()

'''
[문자열 함수]

- upper() 함수: 소문자를 대문자로 변환하는 기능
- lower() 함수: 대문자를 소문자로 변환하는 기능
'''

#  소문자 → 대문자 변환 예제
text05 = "i really like computer"
print(text05)
text05_upper = text05.upper()
print(text05_upper)

print()
print("------------------------")
print()

# 대문자 ↔ 소문자 변환 예제
text06 = "I Don't really Like TO Reading book"
print(text06)

text06_upper = text06.upper()
text06_lower = text06.lower()
print(text06_upper)
print(text06_lower)

print()
print()
print("------------------------")
print("--- 산술 연산자")
print("------------------------")
print()

'''
[연산자]

- 수학적 계산과 데이터 처리를 수행하기 위해 사용하는 기호 또는 기호 조합을 의미.
 
[파이썬에서 지원하는 연산자 종류]

- 산술 연산자: +, -, \*, /, %, //, \*\*
- 대입 연산자: =, +=, -=, \*=, /=
- 비교 연산자: ==, !=, >, <, >=, <=
- 논리 연산자: not, and, or
- 부호 연산자: -

[파이썬에는 없는 연산자]

- ++(증가 연산자), --(감소 연산자)
'''

'''
[연산자]

1. 산술 연산자

- // 나눗셈 몫: a//b a를 b로 나눈 몫
- % 나눗셈 나머지: a&b a를 b로 나눈 나머지
- ** 거듭 제곰: a**b a를 b로 제곱한 결과
- c/c++/java: 나눗셈 몫, 거듭 제곱을 사용하지 않음.
'''

# 예제 1
num01 = 10
num02 = 2

print(num01 + num02)        # 더하기(+): 12
print(num01 - num02)        # 빼기(-): 8
print(num01 * num02)        # 곱하기(*): 20
print(num01 / num02)        # 나누기(/): 5.0
print(num01 % num02)        # 나머지(%): 0
print(num01 // num02)       # 몫 구하기(//): 5
print(num01 ** num02)       # 거듭 제곱 연산자(**) = 10을 2번 곱해라: 100

print()
print("------------------------")
print()

# 예제 2
num03 = 15
num04 = 4

print(num03 + num04)        # 더하기: 19
print(num03 - num04)        # 빼기: 11
print(num03 * num04)        # 곱하기: 60
print(num03 / num04)        # 나누기: 3.75
print(num03 % num04)        # 나머지: 3
print(num03 // num04)       # 몫 구하기: 3
print(num03 ** num04)       # 거듭 제곱: 50625

print()
print()
print("------------------------")
print("--- 대입 연산자")
print("------------------------")
print()

'''
[연산자]

2. 대입 연산자

- 변수에 값을 할당하는 데 사용하는 연산자
- =
'''

# 예제 1
num05 = 77
num06 = 23
num05 = num05 + 23
num06 = num06 - 3

print(num05)
print(num06)

num05 = 77
num06 = 23
num05 += 23
num06 -= 3

print(num05)
print(num06)

print()
print()
print("------------------------")
print("--- 복합 대입 연산자")
print("------------------------")
print()

'''
[연산자]

3. 복합 대입 연산자

- 코드가 간결하다
- 피연산자 : 연산의 대상이 되는 숫자, 변수, 또는 값 자체를 의지
  - ex) a + b = a와 b가 피연산자
  - ex) 10 + 5 = 10, 5가 피연산자
- += : 왼쪽 피연산자에 오른쪽 피연산자를 더한 결과 값을 대입
- -= : 뺀 결과 값을 대입
- \*= : 곱한 결과 값을 대입
- /= : 나눈 결과 값을 대입
- //= : 나눈 몫을 대입
- %= : 나머지 값을 대입
'''

# 예제 1
num07 = 66
num08 = 13
num09 = num07 + num08
num07 += num08
num09 -= num07

print(num07)
print(num08)
print(num09)

print()
print("------------------------")
print()

# 예제 2
num1 = 7
num2 = 3
num3 = num1 // num2
num1 += num2
num3 *= num2

print(num1)
print(num2)
print(num3)

print()
print()
print("------------------------")
print("--- 비교 연산자")
print("------------------------")
print()

'''
[연산자]

4. 비교 연산자

- 두 개의 값을 비교하여 그 결과가 참(true)인지 거짓(false)인지 판별 하는 연산자로, 관계 연산자 라고도 한다.
- 수학적인 부등호처럼 두 값의 관계를 판단 하는 역할.
- \> 크다
- < 작다
- \>= 크거자 같다
- <= 작거나 같다
- == 같다
- != 같지 않다
'''

# 예제 1
a = 70
b = 60

a_is_bigger = a > b
a_is_smaller = a < b
is_equal = a == b
is_not_equal = a != b

print(a_is_bigger)
print(a_is_smaller)
print(is_equal)
print(is_not_equal)

print()
print("------------------------")
print()

# 예제 2
str1 = "abc"
str2 = "a" + "b" + "c"

is_equal2 = (str1 == str2)
print(is_equal2)

one = "1"
num = 1

is_not_equal = (one != num)
print(is_not_equal)

print()
print()
print("------------------------")
print("--- 논리 연산자")
print("------------------------")
print()

'''
[연산자]

5. 논리 연산자

- 논리적인 연산을 수행하여 참인지 거짓인지를 판단하는 연산자
- and: 연산자를 기준으로 왼쪽과 오른쪽 값이 모두 true 일때만 true를 반환, 나머지는 모두 false (&&, &: 다른 언어)
- or: 연산자를 기준으로 왼쪽과 오른쪽 값이 하나라도 true면 true를 반환, 둘다 false일때만 false 반환 (||: 다른 언어)
- not: 뒤에 따라오는 논리값이 true이면 false를 반환, false이면 true를 반환 (!: 다른 언어)
'''

# 예제 1
is_snowing = True
is_cold = True
is_winter = (is_snowing and is_cold)
print(is_winter)

print()
print("------------------------")
print()

# 예제 2
# True는 정수값으로 1, False는 정수값으로 0
is_snowing2 = 1
is_cold2 = 0
is_winter2 = is_snowing2 & is_cold2
print(is_winter2)

print()
print("------------------------")
print()

# 예제 3
is_raining = 1
is_windy = 0
print(is_raining & is_windy)

print()
print()
print("------------------------")
print("--- NOT 연산자")
print("------------------------")
print()

# 예제 1
is_false = False
print(not is_false)

is_true = True
print(not is_true)

print()
print()
print("------------------------")
print("--- 부호 연산자")
print("------------------------")
print()

'''
[연산자]

6. 부호 연산자

- 숫자 앞에 - 부호를 붙여 양수를 음수로, 음수를 양수로 변환할 수 있다.
- 즉, 숫자의 부호를 변경한다.
- ex) x = 10, x = -x, x = -10
'''

# 예제 1
x = 10
x = -x
print(x)

print()
print("------------------------")
print()

#예제 2
x = -x
print(x)

print()
print("------------------------")
print()

# 예제 3
is_true = True
print(- is_true)    # -1

print()
print()
print("------------------------")
print("--- 응용 문제")
print("------------------------")
print()

# 응용 문제 1
y = 10
y *= 7
print(y)

print()
print()
print("------------------------")
print("--- 조건문")
print("------------------------")
print()

'''
[조건문]

- 프로그래밍에서 특정 조건에 따라 프로그램의 흐름을 제어하는 구문을 말한다.
- if / else / elif

[문법]

- 조건식이 참이면 아래 들여쓰기가 된 코드가 순차적으로 실행된다.
if 조건식 :
    실행할 코드 1
    실행할 코드 2
    실행할 코드 3

[주의]
- 파이썬은 들여쓰기가 중요한 언어이다.
- 파이썬에서 들여쓰기는 코드의 블록을 구분하고 가독성을 높이는 데 중요한 역할을 한다.
- {}: 다른언어, 파이썬은 코드 블록을 구성할 중괄호{}를 제공하지 않으므로 들여쓰기로 작성된 코드만을 실행 영역으로 판단하다.
'''

# 조건문(if) 예제 1
if 7 > 1 :
    print("7은 1보다 큽니다.")

print()
print("------------------------")
print()
    
# 조건문(if) 예제 2
if 2 > 5 :
    print("2는 5보다 큽니다.")
else :
    print("2는 5보다 작습니다.")

print()
print("------------------------")
print()

# 조건문(if) 예제 3
age = 20
if age >= 20 :
    print("20세 이상입니다.")

print()
print()
print("------------------------ 끝")
print()

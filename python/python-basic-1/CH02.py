# 2025.03.18 화

print("------------------------")
print()

# 문자열 예제
print(">> 문자열 예제")

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

print("------------------------")
print()

# 문자열 슬라이싱 예제 1
print(">> 문자열 슬라이싱 예제 1")

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

# 문자열 슬라이싱 예제 2
print(">> 문자열 슬라이싱 예제 2")

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

print("------------------------")
print()

# 문자열 길이 예제 1
print(">> 문자열 길이 예제 1")

text03 = "Python"
text03_length = len(text03)
print(text03_length)
print()

# 문자열 길이 예제 2
print(">> 문자열 길이 예제 2")

text04 = "I Love Python"
text04_length = len(text04)
print(text04_length)
print()

print("------------------------")
print()

# 소문자 → 대문자 변환 예제
print(">> 소문자 → 대문자 변환 예제")

text05 = "i really like computer"
print(text05)
text05_upper = text05.upper()
print(text05_upper)
print()

# 대문자 ↔ 소문자 변환 예제
print(">> 대문자 ↔ 소문자 변환 예제")

text06 = "I Don't really Like TO Reading book"
print(text06)

text06_upper = text06.upper()
text06_lower = text06.lower()
print(text06_upper)
print(text06_lower)
print()

print("------------------------")
print()

# 산술 연산자 예제 1
print(">> 산술 연산자 예제 1")

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

# 산술 연산자 예제 2
print(">> 산술 연산자 예제 2")
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

print("------------------------")
print()

# 대입 연산자 예제 1
print(">> 대입 연산자 예제 1")

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

# 복합 대입 연산자 예제 1
print(">> 복합 대입 연산자 예제 1")

num07 = 66
num08 = 13
num09 = num07 + num08
num07 += num08
num09 -= num07

print(num07)
print(num08)
print(num09)
print()

# 복합 대입 연산자 예제 2
print(">> 복합 대입 연산자 예제 2")

num1 = 7
num2 = 3
num3 = num1 // num2
num1 += num2
num3 *= num2

print(num1)
print(num2)
print(num3)
print()

print("------------------------")
print()

# 비교 연산자 예제 1
print(">> 비교 연산자 예제 1")

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

# 비교 연산자 예제 2
print(">> 비교 연산자 예제 2")

str1 = "abc"
str2 = "a" + "b" + "c"

is_equal2 = (str1 == str2)
print(is_equal2)

one = "1"
num = 1

is_not_equal = (one != num)
print(is_not_equal)
print()

print("------------------------")
print()

# 논리 연산자 예제 1
print(">> 논리 연산자 예제 1")

is_snowing = True
is_cold = True
is_winter = (is_snowing and is_cold)
print(is_winter)
print()

# 논리 연산자 예제 2
# True는 정수값으로 1, False는 정수값으로 0
print(">> 논리 연산자 예제 2")

is_snowing2 = 1
is_cold2 = 0
is_winter2 = is_snowing2 & is_cold2
print(is_winter2)
print()

# 논리 연산자 예제 3
print(">> 논리 연산자 예제 3")

is_raining = 1
is_windy = 0
print(is_raining & is_windy)
print()

# NOT 연산자 예제 1
print(">> NOT 연산자 예제 1")

is_false = False
print(not is_false)

is_true = True
print(not is_true)
print()

print("------------------------")
print()

# 부호 연산자 예제 1
print(">> 부호 연산자 예제 1")

x = 10
x = -x
print(x)
print()

# 부호 연산자 예제 2
print(">> 부호 연산자 예제 2")

x = -x
print(x)
print()

# 부호 연산자 예제 3
print(">> 부호 연산자 예제 3")

is_true = True
print(- is_true)    # -1
print()

print("------------------------")
print()

# 응용 문제 1
print(">> 응용 문제 1")
print()

y = 10
y *= 7
print(y)

print("------------------------")
print()

# 조건문(if) 예제 1
print(">> 조건문(if) 예제 1")

if 7 > 1 :
    print("7은 1보다 큽니다.")
print()
    
# 조건문(if) 예제 2
print(">> 조건문(if) 예제 2")

if 2 > 5 :
    print("2는 5보다 큽니다.")
else :
    print("2는 5보다 작습니다.")
print()

# 조건문(if) 예제 3
print(">> 조건문(if) 예제 3")

age = 20
if age >= 20 :
    print("20세 이상입니다.")
print()

print("------------------------")
print()

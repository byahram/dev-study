"""
2025.03.13

- 교재: Mentor Python
- 1. python interpreter 설치
   https://www.python.org/downloads/  --> 버전 3.13.2
- 2. jetbrain pycharm
   https://www.jetbrains.com/pycharm/download/?section=windows
"""

print("------------------------")
print()

# [ 출력문 ]
print("2025-03-13")
print("Hello World!")
print()

print("------------------------")
print()

# >> 변수 선언하기 예제 1
print(">> 변수 선언하기 예제 1")
num = 1
print(num)

firstName = 10
print(firstName)
print()

print("------------------------")
print()

# >> int 정수형 예제 1
print(">> int 정수형 예제 1")
num1 = 100      # int num1 = 100;
num2 = 300      # int num2 = 300;
print(num1)     # 100
print(num2)     # 300
print(num1 + num2)      # 400
print()

# >> int 정수형 예제 2
print(">> int 정수형 예제 2")
a = 500     # int a = 500;
b = 200     # int b = 200;
print(a)
print(b)
print(a * b)
print()

# >> int 정수형 예제 3
# 위에서 이미 사용한 변수명은 아래에서 사용할 수 없다.
# 사용을 하려면 값이 바뀌기 때문에 주의해야 한다.
print(">> int 정수형 예제 3")
num3 = 100
num4 = 300
num5 = num3 + num4
print(num5)
print()

# >> int 정수형 예제 4
print(">> int 정수형 예제 4")
num6 = 500      # int num6 = 500;
num7 = 150      # int num7 = 150
num8 = num6 - num7      # int num8 = num6 - num7
print(num8)
print()

# >> 변수 값 변경하는 예제 1
print(">> 변수 값 변경하는 예제 1")
num01 = 100
num02 = 300
print(num01)
print(num02)
print()

temp = num01    # temp = 100
num01 = num02   # num01 = 300
num02 = temp    # num02 = 100

print(num01)
print(num02)
print()

# >> 변수 값 바꾸는 예제 2
print(">> 변수 값 변경하는 예제 2")
c = 400
d = 600

print(c)
print(d)
print()

temp2 = c
c = d
d = temp2

print(c)
print(d)
print()

print("------------------------")
print()

# >> float 실수형 예제 1
print(">> float 실수형 예제 1")
f01 = 30.5      # float f01 = 30.5
f02 = 25.3      # float f02 = 25.3
print("f01 =", f01)
print("f02 =", f02)

firstFloat = 3.14
print("firstFloat =", firstFloat)
print()

# >> float 실수 사칙 연산 예제 1
print(">> float 실수 사칙 연산 예제 1")
x = 1.7
y = 2.3
print(x + y)
print(x * y)
print()

print("------------------------")
print()

# >> bool 논리형 예제 1
print(">> bool 논리형 예제 1")
k = 100
j = 99
result = k > j
print(result)
print()

# >> bool 논리형 예제 2
print(">> bool 논리형 예제 2")
n01 = 50
n02 = 75
result2 = n01 < n02
print(result2)
print()

print("------------------------")
print()

# 문자열 변수 선언 예제 1
print(">> 문자열 변수 선언 예제 1")
namee = "Kim"       # string name = "Kim"
print(namee)
print()

# 문자열 변수 선언 예제 2
print(">> 문자열 변수 선언 예제 2")
animal = "Cat"
print(animal)
print()

# 문자열 합치기
print(">> 문자열 합치기")
f_Name = "gildong"
l_Name = "Hong"
full_Name = f_Name + l_Name
print(full_Name)
print()

# 문자열 반복하기
print(">> 문자열 반복하기")
hello = "안녕하세요"
print(hello * 3)        # 나눗셈은 불가능하다(덧셈, 곱셈은 가능)
print()

print("------------------------")
print()

# >> 인덱스로 문자 추출하기
print(">> 인덱스로 문자 추출하기")
s = "hello"
f_char = s[0]
t_char = s[2]
print(f_char)
print(t_char)
print()

# >> 개인정보 출력하기
print(">> 개인정보 출력하기")
name = "Alice"
postNum = "12345"
height = "168.5"
print(name)
print(postNum)
print(height)
print()

print("------------------------")
print()

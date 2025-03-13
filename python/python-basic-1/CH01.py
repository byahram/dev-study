"""
2025.03.13

- 교재: Mentor Python
- 1. python interpreter 설치
   https://www.python.org/downloads/  --> 버전 3.13.2
- 2. jetbrain pycharm
   https://www.jetbrains.com/pycharm/download/?section=windows
"""


# [ 주석 ]
# 한줄 주석: 메모장 같은 역할 (프로그램 실행에 영향을 주지 않는다.)
"""
여러줄 주석: 큰 따옴표로 감싸서 사용
"""
'''
여러줄 주석: 작은 따옴표로 감싸서 사용
'''


# [ 출력문 ]
print()
print("2025-03-13")
print("Hello World!")
print()
print("------------------------")


# [ 실행문 ]
# 프로그램이 실제로 동작하면서 각종 작업을 수행하는 코드를 의미
# 즉, 개발자가 컴퓨터에게 내리는 명령이라고 할 수 있다.


# [ 변수란? ]
#   - 필요한 데이터를 메모리라는 임시 저장 공간에 저장한다.
#   - 임시 저장 공간을 우리는 변수라고 한다.
#   - (즉, 데이터를 담아두는 상자)


# [ 변수 선언하기 ]
#   - 프로그램에서 변수를 사용하려면 먼저 변수를 저장할 메모리에 공간을 확보해야 한다. (=변수를 선언한다)
#   - 변수명(상자의 이름표) = 변수값(상자 안에 들어가는 값)
#   - age = 20

# >> 변수 선언하기
print()
print(">> 변수 선언하기")
num = 1
print(num)

# >> 변수 선언하기 예제 1
firstName = 10
print(firstName)
print()
print("------------------------")


# [ 변수 이름 짓는 규칙 ]
#   - 영문, 한글, 숫자 사용 가능
#   - 대소문자를 구분한다. (num, Num)
#   - 변수명의 첫 글자는 숫자로 시작할 수 없다.
#   - 언더바 _를 제외한 특수문자는 사용할 수 없다(!@^^)
#   - 파이썬 예약어를 사용할 수 없다.
#   - 띄어쓰기 불가능


# [ 카멜 케이스 표기법 ]
# 두단어가 합쳐질 때, 두번째 단어의 첫 글자를 대문자로 작성한다. (firstName)


# [ 변수 자료형 ]
# 1. int 정수형
#   - 양의 정수 ,음의 정수, 그리고 0을 포함
#   - ex) -1, 0, 1, 2, 3...

# >> int 정수형 예제 1
print()
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

# >> int 정수형 예제 3
# 위에서 이미 사용한 변수명은 아래에서 사용할 수 없다.
# 사용을 하려면 값이 바뀌기 때문에 주의해야 한다.
print()
print(">> int 정수형 예제 3")
num3 = 100
num4 = 300
num5 = num3 + num4
print(num5)

# >> int 정수형 예제 4
print()
print(">> int 정수형 예제 4")
num6 = 500      # int num6 = 500;
num7 = 150      # int num7 = 150
num8 = num6 - num7      # int num8 = num6 - num7

print(num8)

# >> 변수 값 변경하는 예제 1
print()
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


# 2. float 실수형
#   - 소수와 지수로 구성된 수를 나타내는 자료형
#   - ex) 3.14, 3.15

# >> float 실수형 예제 1
print()
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


# 3. bool 논리형
#   - True 혹은 False의 두 가지 값만 가질 수 있다.
#   - ex) True(참), False(거짓)

# >> bool 논리형 예제 1
print()
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


# 4. String 문자열
#   - 텍스트를 표현하는 데 사용되는 자료형
#   - 작은 따옴표 '', 큰 따옴표 "", 삼중 따옴표를 사용한다
#   - ex) name = "Kim", name = 'Kim'

# 문자열 변수 선언 예제 1
print()
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


# 문자열 인덱스
#   - 문자열의 각 문자는 고유한 번호를 가지며, 이를 인덱스라고 한다.
#   - 각 문자는 칸이 존재한다. 
#   - 인덱스 번호는 0번부터 ㅅ ㅣ작한다.

# >> 인덱스로 문자 추출하기
print()
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

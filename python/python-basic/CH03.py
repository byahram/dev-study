"""
2025.03.20 목
"""

print()
print()
print("------------------------")
print("--- if-else 조건문")
print("------------------------")
print()

'''
[if-else 조건문]

if 조건식:
    조건식이 참일 때 실행할 코드
else :
    조건식이 거짓일 때 실행할 코드
'''

# 예제 1
fruit = "바나나"
if fruit  == "바나나" :
    print("저는 바나나를 좋아합니다.")
else :
    print("저는 바나나를 좋아하지 않습니다.")

print()
print("------------------------")
print()

# 예제 2
number = 17
if number == 17 :
    print("숫자는 17입니다.")
else :
    print("숫자는 17이 아닙니다.")

print()
print("------------------------")
print()

# 예제 3
age = 14
if age >= 20:
    print("20세 이상입니다.")
else :
    print("20세 미만입니다.")

print()
print("------------------------")
print()

# 예제 4
num = 49
if num % 7 == 0 :
    print("num은 7로 나누어 떨어집니다.")
else :
    print("num은 7로 나누어 떨어지지 않습니다.")

print()
print("------------------------")
print()

# 예제 5
num2 = 19
if num2 % 2 == 0 :
    print("num2는 짝수입니다.")
else :
    print("num2는 홀수입니다.")

print()
print()
print("-----------------------------")
print("--- if-elif-else 조건문")
print("-----------------------------")
print()

'''
[if-elif-else 조건문]

- elif: 하나가 아닌 여러 개의 조건 식을 사용할 수 있는 문법

if 조건식1 :
    조건식1이 참일 때
elif 조건식2 :
    조건식2가 참일 때
elif 조건식3 :
    조건식3이 참일 때
else :
    모든 조건이 거짓일 때
'''

# 예제 1
num3 = 0
if num3 > 0 :
    print("양수입니다.")
elif num3 == 0 :
    print("0입니다")
else :
    print("음수입니다.")

print()
print("------------------------")
print()

# 예제 2
score = 87
if score >= 90 :
    print("A")
elif score >= 80 :
    print("B")
elif score >= 70 :
    print("C")
else :
    print("F")

print()
print("------------------------")
print()

# 예제 3
num4 = 0
if num4 % 2 == 0 :
    print("짝수입니다.")
elif num4 % 2 == 1 :
    print("홀수입니다.")
else :
    print("0입니다.")

print()
print()
print("------------------------")
print("--- input()")
print("------------------------")
print()

'''
[input()]

- 파이썬에서 사용자 입력을 받는 방법은 input() 합수를 사용
- 문자 입력 받기
    - name = input("이름을 입력하세요")
    - print("안녕하세요", name, "님!")
- 숫자 입력 받기
    - 정수 > int(input("출력문"))
    - 실수 > float(input("출력문"))
'''

# 예제 1
age2 = int(input("몇살입니까?? >>> "))
if age2 <= 7 :
    print("미취학")
elif age2 <= 13 :
    print("초등학생")
elif age2 <= 16 :
    print("중학생")
elif age2 <= 19 :
    print("고등학생")
else :
    print("성인")

print()
print("------------------------")
print()

# 예제 2
A = int(input("첫번째 숫자: "))
B = int(input("두번째 숫자: "))

if A > B :
    print("출력: >")
elif A < B :
    print("출력: <")
elif A == B :
    print("출력: =")

print()
print("------------------------")
print()

# 예제 3
id = "korea"
password = 1234

if id == "korea" and password == 1234 :
    print("로그인 되었습니다.")
elif id == "korea" and password != 1234 :
    print("비밀번호가 틀렸습니다.")
else :
    print("회원 가입을 진행해 주세요.")

print()
print("------------------------")
print()

# 예제 4
X = int(input("x좌표 : "))
Y = int(input("y좌표 : "))

if X > 0 and Y > 0 :
    print("1")
elif X < 0 and Y > 0 :
    print("2")
elif X < 0 and Y < 0 :
    print("3")
elif X > 0 and Y < 0 :
    print("4")

print()
print("------------------------")
print()

# 예제 5
year = int(input("연도 : "))

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) :
    print("1")
else :
    print("0")

print()
print()
print("------------------------")
print("--- while문")
print("------------------------")
print()

'''
[반복문]

- 여러 줄의 코드 블록을 반복적으로 실행하는데 사용되는 제어 구조
- 반복문을 사용하면 원하는 코드를 원하는 횟수만큼 반복하여 코드를 간결하게 작성하고 효율성을 높일 수 있다.
- for문, while문

1. while문
    - 반복 횟수를 미리 알 수 없는 경우에 사용
    - 조건이 참인 동안 계속해서 코드를 반복한다.
    - 조건이 거짓이 될 때까지 반복

# 조건 식이 true(참)이면 아래 들여쓰기가 되어있는 코드가 순차적으로 실행된다.
while 조건식 :
    조건식이 참이면 실행되는 코드

# 무한 루프
while True :
    print("무한 반복한다")
'''

# 예제 1
count = 0
while count < 3 :
    count = count + 1
    print(count)

print()
print("------------------------")
print()

# 예제 2
count2 = 0
while count2 < 3 :
    print("안녕하세요!")
    count2 += 1

print()
print("------------------------")
print()

# 예제 3
count3 = 9
while count3 > 4 :
    print(count3)
    count3 -= 1

print()
print("------------------------")
print()

# 예제 4
money = 5000
while money >= 3000 :
    print("아이스크림을 사먹었습니다.")
    money -= 1000

print()
print("------------------------")
print()

# 예제 5
money2 = 5000
priceOfCandy = 700
numOfCandy = 0

while money2 >= 700:
    money2 -= priceOfCandy
    numOfCandy += 1
    print("사탕을", numOfCandy,  "개 사 먹었습니다.")
print("남은 돈: ", money2, "원")

print()
print()
print("----------------------------------")
print("--- while문을 사용하여 별 찍기")
print("----------------------------------")
print()

# 예제 1
i = 1
while i < 6 :
    print("*" * i)
    i += 1

print()
print("------------------------")
print()

# 예제 2
i2 = 5
while i2 > 0:
    print("*" * i2)
    i2 -= 1

print()
print()
print("------------------------ 끝")
print()

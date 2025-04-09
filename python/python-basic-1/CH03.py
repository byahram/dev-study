"""
2025.03.20 목
"""

print()
print()
print("------------------------")
print("--- if-else 조건문")
print("------------------------")
print()

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

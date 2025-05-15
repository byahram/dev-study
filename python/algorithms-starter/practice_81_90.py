# 81. 잔돈 구하기
print("[81.]")
a = 47200
case_10000 = a // 10000
case_5000 = a % 10000 // 5000
case_1000 = a % 10000 % 5000 // 1000
case_500 = a % 10000 % 5000 % 1000 // 500
case_100 = a % 10000 % 5000 % 1000 % 500 // 100

print("잔돈 :", a)
print("10000원권 :", case_10000)
print("5000원권 :", case_5000)
print("1000원권 :", case_1000)
print("500원권 :", case_500)
print("100원권 :", case_100)
print()

# 82. 일당 계산기
print("[82.]")
hours = 10
money = 9160
overtime = 1.5 * money

if hours > 8:
    print("오늘 일당은 {}원입니다.".format(8 * money + (hours - 8) * overtime))
else:
    print("오늘 일당은 {}원입니다.".format(hours * money))
print()

# 83. 구구단 출력하기 
print("[83.]")
for i in range(2, 10):
    print("<" + str(i) + "단>")

    for j in range(1, 10):
        print(i, "X", j, "=", i*j)

        if j ==9:
            print(" ")
print()

# 84. 반복문 응용 - 숫자 찍기 1 
print("[84.]")
for i in range(5, 0, -1):
    for j in range(i):
        print("1", end="")
    print("")
print()

# 85. 반복문 응용 - 숫자 찍기 2 
print("[85.]")
for i in range(5):
    for j in range(i+1):
        print("0", end="")
    for j in range(5-i):
        print("1", end="")
    print("")
print()

# 86. 반복문 응용 - 숫자 찍기 3 
print("[86.]")
for i in range(1, 6):
    for j in range(5-i):
        print(0, end="")
    for j in range(1, i*2):
        print(1, end="")
    for j in range(5-i):
        print(0, end="")
    print()
for i in range(5):
    for j in range(i):
        print(0, end="")
    for j in range(10, 1+i*2, -1):
        print(1, end="")
    for j in range(i):
        print(0, end="")
    print()
print()

# 87. 반복문 응용 - 숫자 찍기 4 
print("[87.]")
for i in range(5):
    for j in range(i):
        print(0, end="")
    for j in range(10, 1+i*2, -1):
        print(1, end="")
    for j in range(i):
        print(0, end="")
    print("")
for i in range(2, 6):
    for j in range(5 - i):
        print(0, end="")
    for j in range(1, i*2, 1):
        print(1, end="")
    for j in range(5-i):
        print(0, end="")
    print("")
print()

# 88. 배수의 총합 구하기
print("[88.]")
n = 1000
sum = 0
for i in range(1, n):
    if i % 3 == 0 or i % 5 == 0:
        sum += i
print(sum)
print()

# 89. 소인수분해 구현하기 
print("[89.]")
num = 24
print("num = ", end="")

while True:
    i = 2
    while True:
        if num % i == 0:
            num /= i
            print(i, end="")
            break
        else:
            i += 1
    if num == 1:
        break
    else:
        print(" * ", end="")
print("\n")

# 90. 간단한 함수 구현하기 
print("[90.]")
def hello(name) :
    print(f"{name}님 안녕하세요.")
hello("홍길동")
print()

# 71. 조건문 if, elif, else 
print("[71.]")
num = 5
if num > 0 :
    print("양수입니다.")
elif num < 0 :
    print("음수입니다.")
else :
    print("0 입니다.")
print()

# 72. 조건 및 분기문 사용하기
print("[72.]")
age = 17
if age <= 13 :
    print("삐빅, 어린이입니다.")
elif 14 <= age <= 19 :
    print("삐빅, 청소년입니다.")
elif age >= 20 and age <= 34 :
    print("삐빅, 청년입니다.")
elif age >= 35 and age <= 64 :
    print("삐빅, 중장년입니다.")
else :
    print("삐빅, 노인입니다.")
print()

# 73. 가장 큰 수 찾는 프로그램 만들기
print("[73.]")
num1 = 15
num2 = 23
num3 = 9

if (num1 > num2) and (num1 > num3) :
    print("가장 큰 수를 가지고 있는 변수는 값이 %d인 num1입니다." % num1)
elif (num2 > num1) and (num2 > num3) :
    print("가장 큰 수를 가지고 있는 변수는 값이 %d인 num2입니다." % num2)
elif (num1 == num2 == num3) :
    print("모두 같은 수 입니다.")
else :
    print("가장 큰 수를 가지고 있는 변수는 값이 %d인 num3입니다." % num3)
{}
print()

# 74. 시험 합격 / 불합격 프로그램
print("[74.]")
A_CLASS = [70, 60, 90, 80, 100, 50, 80, 90, 45, 100]

count_pass = 0
count_100 = 0

for i in A_CLASS :
    if i >= 70 :
        count_pass += 1
        if i == 100 :
            count_100 += 1
count_fail = len(A_CLASS) - count_pass

print("전체 {}명의 학생 중 총 합격자는 {}명이고 그 중 만점자는 {}명입니다. 아쉽게 불합격한 학생은 {}명입니다.".format(len(A_CLASS), count_pass, count_100, count_fail))
print()

# 75. 피보나치 수열 구현하기
# 초항이 0이고 두번째는 1, 그 이후는 이전의 두 수를 더한 값을 가진다.
print("[75.]")
n = 12
f = []

for i in range(0, n) :
    if i == 0 :
        f.append(0)
    elif i == 1 :
        f.append(1)
    else :
        fibo = (f[i-1]) + (f[i-2])
        f.append(fibo)

print(f)
print()

# 76. 반올림 프로그램
print("[76.]")
num =  17
if num % 10 < 5 :
    print("반올림 결과 : {}".format(num - (num % 10)))
else :
    print("반올림 결과 : {}".format(num + (10 - (num % 10))))
print()

# 77. 조건문, 윤년 판별 프로그램
print("[77.]")
year = 2022
if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0) :
    print("{}년은 윤년입니다.".format(year))
else :
    print("{}년은 윤년이 아닙니다.".format(year))
print()

# 78. 주차별 다이어트 프로그램
print("[78.]")
weight = 131
i = 1
while weight >= 100 :
    print("{}주차 몸무게 : {}".format(i, weight - 2))
    weight -= 2
    i += 1
print("%dkg 달성 성공! 축하드립니다!" % weight)
print()

# 79. 반복문과 조건문을 이용한 수학식
print("[79.]")
sum = 0
for i in range(1, 101) :
    if i % 2 == 1 :
        sum += i
    else :
        sum -= i
print(sum)
print()

# 80. 반복문을 이용한 수학식
print("[80.]")
sum = 0
j = 1

for i in range(55, 0, -1) :
    sum += i * j
    j += 1
print(sum)
print()

"""
2025.04.15 화
"""

print()
print()
print("------------------------")
print("--- 모듈")
print("------------------------")
print()

'''
[모듈]

- 파이썬 코드가 들어있는 '도구상자'
- 우리가 자주 쓰는 코드들을 모아 놓은 파일들
- .py로 끝나는 파이썬 파일 하나하나 모두 다 모듈이다.

[왜 모듈을 사용할까?]

- 자주 쓰는 기능을 쉽게 써내 쓰기 위해서 사용한다.

[상수]

- 변하지 않는 값이다.
- 용도 : 고정된 숫자, 기준값 등
- '대문자'로 이름을 쓰면 상수라고 본다.

[return을 쓰는 이유?]

- 답을 돌려 주는 역할
- 함수에서 결과를 밖으로 보내 주는 버튼
- 함수는 어떤 입력값을 받아서 계산하고, 
  그 결과를 밖으로 보내줘야 다른 데에서 쓸 수 있는데 그 역할이 바로 return이다.
'''

# EX1
# 파이썬에서 다른 파일에 있는 코드를 가져오고 싶을 때, import를 사용한다.
import CH12_01

# EX1.
min = CH12_01.hour_to_min(6)
print("6 hours =", min, "min")

sec = CH12_01.min_to_sec(12)
print("12 minutes =", sec, "sec")

sec2 = CH12_01.hour_to_sec(3)
print("3 hours =", sec2, "sec")

print()
print("------------------------")
print()

# EX2.
numOfApple = 3
price = CH12_01.pay_for_apples(numOfApple)
print("사과", numOfApple, "개의 가격은", price, "원입니다.")

print()
print("------------------------")
print()

'''
[from 모듈명 import 불러오고 싶은 함수명]

- from은 특정 도구상자(모듈)에서 필요한 것만 골라서 가져올 때 사용하는 방법

[from 왜 쓰는가?]

1. 필요한 것만 가져오고 싶을 때
2. 코드가 더 짧아지고 깔끔해진다.
'''

# EX3.
# from CH12_01 import hour_to_min, min_to_sec
from CH12_01 import *      # * : 애스터리스크 -> 모듈 내 모든 함수를 사용하고 싶은 경우

min = hour_to_min(7)
print("7 hours =", min, "min")

sec = min_to_sec(13)
print("13 minutes =", min, "sec")

print()
print("------------------------")
print()

# EX4.
# Section12_Module 패키지의  <EX12_07> 모듈에서 모든 함수와 변수를 가져온다.
from CH12_Module.CH12_03 import *

fat_calories = calculate_calories(1, 10)
print(fat_calories)

protein_cal = calculate_calories(2, 20)
print(protein_cal)

other_cal = calculate_calories(10, 7)
print(other_cal)

print()
print("------------------------")
print()

# EX5.
from CH12_Module.CH12_03 import *

coke = calculate_sugar(1, 250)
print(f"탄산음료 250ml에 들어있는 당 : {coke}g")

juice = calculate_sugar(2, 200)
print(f"과일주스 200ml에 들어있는 당 : {juice}g")

other = calculate_sugar(10, 100)
print(other)

print()
print()
print("----------------------------")
print("--- 표준 모듈: 1. math")
print("----------------------------")
print()

"""
[표준 모듈]

- 기본으로 제공하는 모듈을 우리는 표준 모듈이라고 한다.
- 표준 모듈은 파이썬을 설치할때 자동으로 설치된다.
- import 키워드만으로 바로 사용할 수 있다.

[종류]

1. math 모듈 : 수학 관련 함수 제공 (제곱근, 삼각함수, 로그 계산)
2. random 모듈 : 난수 생성관련 함수 제공 (리스트 요소 랜덤 추춘, 범위 내 난수 추출등)
3. datetime 모듈 : 날짜 및 시간 관련 함수. (날짜 형식변환, 시간 계산 등)
"""

"""
[표준 모듈: 1. math]
"""

import math

# math 모듈을 활용하여 원의 둘레 구하기
def calculate_cal(radius) :
    # math.pi :  수학 관련 모듈 안에 pi를 이용하여 원주율 값을 가져온다.
    cir = 2 * math.pi * radius
    return cir

# 반지름 입력 받기
radius = float(input("원의 반지름을 입력하세요 : "))

# 함수를 호출해서 원의 둘레를 반환받기
cir = calculate_cal(radius)
print("입력하신 원의 둘레는 ", cir, "입니다.")

print()
print("------------------------")
print()

'''
[math 모듈 안에 있는 함수]

1. ceil(n) 함수 : n을 올림하여 가장 가까운 정수로 반환
2. floor(n) 함수 : n을 내림하여 가장 가까운 정수로 반환
3. trunc(n) 함수 : n을 소수점 이하를 버리고 정수 부분만 반환
4. round(n) 함수 : n을 가장 가까운 정수로 반올림하여 반환
5. sqrt(n) 함수 : n의 제곱근을 반환
    - 예시 : math.sqrt(9)     = 3
6. pow(n, m) 함수 : n을 m번 거듭제곱한 값을 반ㄴ환
    - math.pow(2, 3)      = 8
'''

# 올림 처리하여 반환
print("[올림] 1.2를 올림 처리하면 :", math.ceil(1.2))
print("[올림] -3.5를 올림 처리하면 :", math.ceil(-3.5))
print()

# 내림 처리하여 반환
print("[내림] 1.7을 내림 처리하면 :", math.floor(1.7))
print("[내림] -2.7을 내림 처리하면 :", math.floor(-2.7))
print()

# 소수점 이하를 버리고 반환
print("[버림] 1.3의 소수점 이하를 버리면 :", math.trunc(1.3))
print("[버림] -2.3의 소수점 이하를 버리면 :", math.trunc(-2.3))
print()

# 버림 : 소수점 이하는 그냥 잘라버린다. 양수든 음수든 자르기만 한다.
# 내림 : 무조건 아래쪽(작은 정수)로 내려간다. 양수는 그대로지만 음수는 더 작아진다.
print("[버림]", math.trunc(-2.7))
print("[내림]", math.floor(-2.7))
print()

# 반올림
print("[반올림]", round(3.6))
print("[반올림]", round(3.2))
print()

# 소수점 자리수 지정 가능
# 문법 : round(소수점, 자리수)
print("[반올림 자리수 지정]", round(3.14159, 2))
print()

# 제곱근을 구하는 함수
number = 49
result_sqrt = math.sqrt(number)
print("[제곱근]", result_sqrt)
print()

# 거듭제곱을 구하는 함수
result_pow = math.pow(2, 10)
print("[거듭제곱]", result_pow)

print()
print()
print("------------------------------")
print("--- 표준 모듈: 2. random")
print("------------------------------")
print()

"""
[표준 모듈: 2. random 모듈]

- 난수를 생성해주는 random 모듈
- 간단한 게임을 제작하는 것은 물론 확률을 처리하거나 데이터를 유니크하게 만드는 데 활용한다.

[random 모듈 함수]

1. random.randint(a, b) 
    - a와 b 사이의 범위에서 임의의 정수를 하나 생성한다.
2. random.randrange(start, stop, step)
    - start부터 stop 이전까지 step 간격으로 임의의 정수를 하나 생성한다. start는 생략가능하고 default값은 0이다.
3. random.sample(시퀀스자료형, 원하는 개수)
    - 인덱스(위치 번호)를 가지고 있다.
    - 리스트나 문자열 같은 시퀀스 자료형에서, 원하는 개수만큼 '중복 없이 랜덤으로' 뽑아주는 함수다.
4. choice(시퀀스 자료형)
    - 시퀀스 자료형의 요소 중 하나를 임의로 반환한다.
5. random.shuffle(시퀀스 자료형)
    - 리스트 안에 있는 값들의 순서를 랜덤으로 섞어주는 함수

[시퀀스 자료형]

- 정의: 여러 개의 값을 순서대로 저장하는 자료형
- 대표적인 시퀀스 자료형 : 
    - 문자열    "hello" 글자들이 순서대로 모인것
    - 리스트    [1, 2, 3] 여러 데이터로 순서대로 저징
    - 튜플      (10,20,30) : 리스트처럼 생겼지만 수정 불가
    - range     range(5) : 순서대로 증가하는 숫자들
- 시퀀스 자료형의 공통 특징
    1. 인덱스로 값에 접근할 수 있다.
    2. 반복문으로 하나씩 꺼내 쓸 수 있다.
    3. len() 함수로 길이를 알 수 있다.
    4. +, * 연산도 가능하다.
"""

import random

# EX1.
# 두 인수 (1~45)사이의 정수를 임의로 생성하여 반환
print(random.randint(1, 45))            # 1 이상 34이하의 정수

# 두 인수 사이의 특정 조건을 가지는 정수 중 임의의 수를 반환한다.
print(random.randrange(10))             # 0 이상 10 미만의 정수
print(random.randrange(1, 20, 2))       # 1 이상 20 미만의 홀수

# 로또 번호 생성기
def generate_lotto() :
    # 1부터 45 사이의 숫자 중 6개를 임의로 선택하여 리스트에 저장한다.
    lotto = random.sample(range(1, 46), 6)
    return lotto

lotto_numbers = generate_lotto()
print("로또 번호 :", lotto_numbers)

print()
print("------------------------")
print()

# EX2. 뽑기 게임 만들기
# 랜덤으로 당첨자 뽑아
def generate_win(person) :
    winner = random.choice(person)
    return winner

# 빈 리스트 생성
list_persons = []

# 5명의 참가자를 입력 받아 리스트에 추가
for p in range(1, 6) :
    person = input("참여할 사람들을 입력하세요 >> ")
    list_persons.append(person)

print("아이스크림 내기에 참여할 사람들은", list_persons, "입니다")

# 당첨자 뽑기 및 출력
winner = generate_win(list_persons)
print("내기에 걸린 사람은", winner, "입니다.")

print()
print("------------------------")
print()

# EX3. 가위바위보 게임 만들기
# 3판 2선승
options = ["가위", "바위", "보"]

# 승수 저장
user_win = 0
computer_win = 0

print("가위 바위 보 게임 시작~!")
print()

while user_win < 2 and computer_win < 2 :
    # 사용자 입력 추가
    user_choice = input("가위 바위 보 중에 하나를 입력하세요 >> ")
    # 컴퓨터
    computer = random.choice(options)

    print()
    print(f"컴퓨터 = {computer}")
    print(f"사용자 = {user_choice}")
    print()

    # 승부 판단
    if user_choice == computer :
        print("비겼습니다.\n")
    elif ((user_choice == "가위" and computer == "보") or \
        (user_choice == "바위" and computer == "가위") or \
        (user_choice == "보" and computer == "바위"))  :
        print("사용자 승!\n")
        user_win += 1
    elif user_choice in options :
        print("컴퓨터 승!\n")
        computer_win += 1
    else :
        print("입력이 올바르지 않습니다. 다시 입력해 주세요. \n")

    print(f"현재 스코어 → 사용자 : {user_win}승 / 컴퓨터 : {computer_win}승\n")

# 게임 결과 출력
if user_win == 2 :
    print("사용자 최종 승리!")
else :
    print("컴퓨터 최종 승리!")

print()
print("------------------------")
print()

# EX4.
myList = [1, 2, 3, 4, 5]
random.shuffle(myList)
print(myList)       # 순서가 섞인 결과가 출력된다.

students = ["씨언어", "파이썬", "자바", "씨쁠쁠"]
random.shuffle(students)
print(students)

print()
print()
print("------------------------------")
print("--- 표준 모듈: 3. datetime")
print("------------------------------")
print()

"""
[표준 모듈: 3. datetime 모듈]

- 오늘 날짜를 출력하거나, 두 날짜 사이의 시간 차이를 계산하는 등 다양한 작업을 할 수 있다.
"""

import datetime

# 현재 날짜 및 시간 반환
dateTimeToday = datetime.datetime.now()
print(dateTimeToday)

# 날짜만 떼어서 사용하기
print("오늘 날짜는 ", dateTimeToday.date(), "입니다.")

# 년도 출력하기
print("지금은", dateTimeToday.year, "년 입니다.")

# 시간 가져오기
now = datetime.datetime.now()
print("집에 갈 시간", now)

print()
print()
print("------------------------ 끝")
print()
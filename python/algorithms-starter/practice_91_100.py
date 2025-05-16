# 91. 주식 수익률 프로그램 
print("[91.]")
def stocks(buy, sell, shares):
    rate = sell / buy * 100 - 100
    income = (sell - buy) * shares
    return income, rate

print(stocks(66400, 80000, 100))
print()

# 92. 함수 설명서 만들기 
print("[92.]")
def stocks2(buy, sell, shares):
    '''
    매수가격(sell)과 매도가격(buy), 수량(shares)을 매개변수로 가지고 
    총손익(income)과 수익률(rate)을 반환하는 stock() 함수입니다.
    rate = sell / buy * 100 - 100
    income = (sell - buy) * shares
    '''
    rate = sell / buy * 100 - 100
    income = (sell - buy) * shares 
    return income, rate

help(stocks2)
print()

# 93. 사용자 정의 함수 - 문자열 reverse 
print("[93.]")
def reverse_print(txt):
    print(txt[::-1])

reverse_print("홍길동은 지금 몹시 화가 났다.")
print()

# 94. 점심 메뉴 추천 프로그램 
print("[94.]")
import random
lunch = ["김치찌개", "짜장면", "김밥", "햄버거", "순대국밥", "한식뷔페", "샐러드"]

def lunch_reco(menu):
    index = random.randint(0, len(menu) - 1)
    print("추천메뉴는!! %s입니다." % menu[index])

lunch_reco(lunch)
print()

# 95. 숫자 마름모 그리기 
print("[95.]")
def rhombus(n):
    for i in range(1, n+1):
        for j in range(n-i):
            print(0, end="")
        for j in range(1, i*2):
            print(1, end="")
        for j in range(n-i):
            print(0, end="")
        print()
    for i in range(n):
        for j in range(i):
            print(0, end="")
        for j in range(n*2, 1+i*2, -1):
            print(1, end="")
        for j in range(i):
            print(0, end="")
        print()

rhombus(10)
print()

# 96. 숫자 사각형 그리기 
print("[96.]")
def square(num):
    for i in range(1, num+1):
        for j in range(1, num+1):
            if i * j < 10:
                print(0, end="")
            print(i*j, end=" ")
        print()

square(9)
print()

# 97. 한글로 한자 찾는 함수 
print("[97.]")
LastName = {
    "김": "金",
    "이": "李",
    "박": "朴",
    "최": "崔",
    "정": "鄭",
    "조": "趙",
    "강": "姜",
    "윤": "尹",
    "장": "張",
    "임": "林"
}

def Search(text):
    K = list(LastName)
    
    for i in range(0, len(K) + 1):
        if text == K[i]:
            return print(LastName[text])
        else:
            return print("찾을 수 없는 성씨입니다.")

Search("김")
Search("마이클")
print()

# 98. BMI를 이용한 비만도 구하기
print("[98.]")
def BMItest(cm, kg):
    BMI = kg / (cm / 100) ** 2
    result = ["저체중", "정상", "과체중", "비만"]

    if BMI <= 18.5:
        print("{}입니다. (BMI지수: {:.2f}%)".format(result[0], BMI))
    elif 18.5 < BMI <= 22.9:
        print("{}입니다. (BMI지수: {:.2f}%)".format(result[1], BMI))
    elif 23 <= BMI <= 24.9:
        print("{}입니다. (BMI지수: {:.2f}%)".format(result[2], BMI))
    elif 25 <= BMI:
        print("{}입니다. (BMI지수: {:.2f}%)".format(result[3], BMI))

BMItest(170, 73)
print()

# 99. 로또 번호 추첨 구현하기 
print("[99.]")
import random

lotto = []
while True:
    num = random.randint(1, 45)
    if num not in lotto:
        lotto.append(num)
    if len(lotto) == 7:
        break

lotto.sort()
print("<파이썬으로 만든 로또 번호 생성기>")
print("당첨번호 :", end="")

for i in lotto[0:6]:
    print(i, end=" ")
print(" 보너스 :", lotto[6])
print()

# 10. datetime 모듈 사용하기 
print("[100.]")
import datetime

end = datetime.datetime.now()
print(end)
print("파이썬 문제풀이 공부가 끝났습니다. 수고하셨습니다.")
print()

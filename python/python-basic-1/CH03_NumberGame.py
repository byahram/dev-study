"""
2025.03.20 목 - NumberGame
"""
import random       # 랜덤 숫자 생성 모듈

# 1부터 100사이의 랜덤 숫자 생성
secret_numbers = random.randint(1, 100)

# 사용자 입력 변수
guess = 0       # 초기값 설정
count = 0       # 시도 횟수 기록

print("1부터 100사이의 숫자를 맞춰보세요!")

# 정답을 맞출 때까지 반복
while guess != secret_numbers:
    # 사용자 입력 받기
    guess = int(input("숫자를 입력하세요 : "))
    count += 1      # 시도 횟수 증가

    if guess < secret_numbers :
        print("값이 너무 작습니다. 더 큰 숫자를 입력하세요.")
    elif guess > secret_numbers :
        print("값이 너무 큽니다. 더 작은 숫자를 입력하세요.")
    else :
        print(f"축하합니다! {count}번 만에 숫자를 맞췄습니다!")

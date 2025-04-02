"""
2025.04.01 화
"""

print()
print()
print("------------------------")
print("--- 함수")
print("------------------------")
print()

# EX1.
print("# EX1.")

def hello() :
    print("안녕하세요")
    print("제 이름은 파이썬입니다.")

hello()
print()
hello()

print()
print()
print("------------------------")
print("--- 지역변수")
print("------------------------")
print()

# EX1.
print("# EX1.")

def greet() :
    message = "hello"       # 지역변수
    print(message)
greet()
print()

# EX2.
print("# EX2.")

def show_score() :
    score = 95
    print(score)
show_score()

print()
print()
print("------------------------")
print("--- 전역변수")
print("------------------------")
print()

# EX1.
print("# EX1.")

score = 0
def add_score() :
    # 만약 global을 삭제한다면? : 함수 안에 있는 score를 지역변수로 생각하는데, 아직 값이 없어서 오류가 난다.
    global score    # 함수 안에서 전역변수를 사용하겠다고 선언
    score += 10
    print("함수 안 점수 : ", score)

add_score()
print("함수 밖 점수 : ", score)
print()

# EX2. 게임 점수 시스템
print("# EX2. 게임 점수 시스템")

score = 100
def play_game() :
    scoreNum = 0        # 지역 변수 
    print("게임 시작 ", scoreNum)
    scoreNum += 50
    print("게임 시작 ", scoreNum)

play_game()
print()

# EX3. 게임 점수 시스템
print("# EX3. 게임 점수 시스템")

score = 100
def playing() :
    global score
    score = 0
    print("게임 시작! ", score)
    score += 50
    print("아이템 획득! ", score)
    print("게임 시작! ", score)
    
playing()

print()
print()
print("------------------------")
print("--- 매개변수")
print("------------------------")
print()

# EX1. 매개변수
print("# EX1.")

def say_hello(name) :
    print("안녕, ", name)

# 인자 : 함수를 호출할 때 전달하는 실제 값
say_hello("민지야")         # 매개변수에는 name = "민지"
say_hello("민주")           # 매개변수에는 name = "민주"
print()

# EX2. 두 수 더하기
print("# EX2. 두 수 더하기")

def add(a, b) :
    print("두수의 합 = ", a + b)

add(10, 15)
print()

# EX3. 매개변수
print("# EX3. 매개변수")

def hello(name) :
    print("안녕하세요!")
    print("제 이름은 " + name + "입니다")
    print("만나서 반갑습니다.")

hello("김송아")
print()

# EX4.
print("# EX4.")

def multiply(num1, num2) :      # 매개변수(=parameter)
    print(num1 * num2)

multiply(3, 4)      # 인자
print()

# EX5.
print("# EX5.")

def introduce(name, age) :
    print("안녕하세요, 제 이름은 ", name, "입니다")
    print("제 나이는 ",  age, "입니다")
    print("잘 부탁드립니다.")

introduce("제니", 20)

print()
print()
print("------------------------")
print("--- return")
print("------------------------")
print()

# EX1.
print("# EX1.")

def add2(a, b) :
    print(a + b)
add2(3, 5)

# return을 쓰는 경우
def add3(a, b) :
    return a + b            # 함수 밖으로 더한 값을 내보내고 싶다.

result = add3(3, 5)
print(result) 
print()

# EX2.
print("# EX2.")

def multiply2(x, y) :
    return x * y

result = multiply2(4, 6)
print(result)

print()
print()
print("------------------------")
print("--- 매개변수의 경우의 수")
print("------------------------")
print()

# EX1.
print("# EX1.")

def get_number() :
    return 42

num = get_number()
print(num)
print()

# EX2.
print("# EX2.")

def add5(a, b) :
    return a + b

result = add5(3,5)
print(result)
print()

# EX3.
print("# EX3.")

def plus(a, b) :
    return a + b

sum = plus(5, 10)
print(sum)
print()

# EX4.
print("# EX4.")

def plus_add(a, b) :
    sum = a + b
    if sum % 2 == 0 :
        return sum
    else :
        return sum + 1

print(plus_add(5, 10))
print(plus_add(6, 10))   
print()

# EX5. 세 수 중 가장 큰 수를 반환하기
print("# EX5. 세 수 중 가장 큰 수를 반환하기")

# max() 함수는 여러 값 중에서 가장 큰 값을 찾아서 돌려주는 함수이다.
# min() 함수는 가장 작은 값을 돌려주는 함수이다.

def find_max(a, b, c) :
    # max = a
    # if b > max :
    #     return b
    # elif c > max :
    #     return c
    # else :
    #     return a
    return max(a, b, c)

print(find_max(3, 7, 5))
print(find_max(10, 2, 8))
print()

# EX6. 리스트에서 최댓값 찾기
print("# EX6. 리스트에서 최댓값 찾기")

scores = [82, 91, 77, 88]
print(max(scores))
print(max("a", "z", "c"))       # 아스키코드표에 의해서 결과가 나온다. a:97, z: 122
print()

# EX7.
print("# EX7.")

def check_seven(num) :
    if num % 7 == 0 :
        return True
    else :
        return False
    
print(check_seven(3))

print()
print()
print("------------------------")
print("--- 팩토리얼")
print("------------------------")
print()

# EX1.
print("# EX1.")

def factorial(num) :
    sum = 1     # 지역 변수

    # range(5)는 [0, 1, 2, 3, 4]
    for n in range(num) :
        sum = sum * (n+1)       # [1, 2, 3, 4, 5]
        # sum = sum * (0 + 1) = 1
        # sum = sum * (1 + 1) = 1 * 2 = 2
        # sum = sum * (2 + 1) = 2 * 3 = 6
        # sum = sum * (3 + 1) = 6 * 4 = 24
        # sum = sum * (4 + 1) = 24 * 5 = 120
    return sum

print(factorial(5))

print()
print()
print("------------------------")
print("--- 심화 예제")
print("------------------------")
print()

# EX1. 리스트로 평균 반환하기
print("# EX1. 리스트로 평균 반환하기")

def cal_average(scores) :
    sum = 0

    for score in scores :
        sum += score

    average = sum / len(scores)
    return average

average1 = cal_average([55, 70, 100])
print(average1)
print()

# EX2. 리스트 숫자 두 배로 출력하기
print("# EX2. 리스트 숫자 두 배로 출력하기")

def double_numbers(numbers) :
    new_list = []
    for num in numbers :
        new_list.append(num * 2)
    return new_list

list = double_numbers([3, 5, 7])
print(list)
print()

# EX3. 리스트에서 최댓값 반환하기
print("# EX3. 리스트에서 최댓값 반환하기")

def find_max(numbers) :
    max_value = numbers[0]

    for n in numbers :
        if n > max_value :
            max_value = n

    return max_value

max1 = find_max([45, 89, 72, 33, 100])
print(max1)

print()
print()
print("------------------------")
print("--- 파일 관련 함수")
print("------------------------")
print()

import os
print(os.getcwd())

# 파일 읽기
file = open("./python/python-basic-1/ch07.txt", "r", encoding="utf-8")
all = file.read()
print(all)

# 파일 쓰기
file = open("./python/python-basic-1/ch07.txt", "w")
file.write("ABCDEFC")

# 파일 닫기
file = open("./python/python-basic-1/ch07.txt", "r")
all = file.read()
print(all)
file.close()        # 운영체제에서 파일을 닫는다(시각적으로 변화하는 것은 아님)

print()
print()
print("------------------------")
print("--- 콜백함수")
print("------------------------")
print()

"""
- 나중에 불려지는 함수
- 다른 함수에 인자로 전달되는 함수이고, (나중에 필요할 때) 호출되는 함수를 말한다.
- 쉽게 말하자면? 나 이 함수 나중에 불러줘 하는거고 다른 함수에게 맡겨두는 함수이다.
"""
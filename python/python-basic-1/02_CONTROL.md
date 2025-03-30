# [Python1] 제어 구조

<br>

## 조건문

- 프로그래밍에서 특정 조건에 따라 프로그램의 흐름을 제어하는 구문을 말한다.
- if / else / elif

### 조건문 문법

- 조건식이 참이면 아래 들여쓰기가 된 코드가 순차적으로 실행된다.

```python
if 조건식 :
    실행할 코드 1
    실행할 코드 2
    실행할 코드 3
```

- 파이썬은 들여쓰기가 중요한 언어이다.
- 파이썬에서 들여쓰기는 코드의 블록을 구분하고 가독성을 높이는 데 중요한 역할을 한다.
- {}: 다른언어, 파이썬은 코드 블록을 구성할 중괄호{}를 제공하지 않으므로 들여쓰기로 작성된 코드만을 실행 영역으로 판단하다.

```python
# EX1
if 7 > 1 :
    print("7은 1보다 큽니다.")      # 7은 1보다 큽니다.

# EX2
if 2 > 5 :
    print("2는 5보다 큽니다.")
else :
    print("2는 5보다 작습니다.")        # 2는 5보다 작습니다.

# EX3
age = 20
if age >= 20 :
    print("20세 이상입니다.")       # 20세 이상입니다.
```

### if-else 조건문

```python
if 조건식:
    조건식이 참일 때 실행할 코드
else :
    조건식이 거짓일 때 실행할 코드
```

```python
# EX1
fruit = "바나나"
if fruit  == "바나나" :
    print("저는 바나나를 좋아합니다.")          # 저는 바나나를 좋아합니다.
else :
    print("저는 바나나를 좋아하지 않습니다.")

# EX2
number = 17
if number == 17 :
    print("숫자는 17입니다.")           # 숫자는 17입니다.
else :
    print("숫자는 17이 아닙니다.")

# EX3
age = 14
if age >= 20:
    print("20세 이상입니다.")
else :
    print("20세 미만입니다.")           # 20세 미만입니다.

# EX4
num = 49
if num % 7 == 0 :
    print("num은 7로 나누어 떨어집니다.")           # num은 7로 나누어 떨어집니다.
else :
    print("num은 7로 나누어 떨어지지 않습니다.")

# EX5
num2 = 19
if num2 % 2 == 0 :
    print("num2는 짝수입니다.")
else :
    print("num2는 홀수입니다.")         # num2는 홀수입니다.
```

### if-elif-else 조건문

- elif: 하나가 아닌 여러 개의 조건 식을 사용할 수 있는 문법

```python
if 조건식1 :
    조건식1이 참일 때
elif 조건식2 :
    조건식2가 참일 때
elif 조건식3 :
    조건식3이 참일 때
else :
    모든 조건이 거짓일 때
```

```python
# EX1
num3 = 0
if num3 > 0 :
    print("양수입니다.")
elif num3 == 0 :
    print("0입니다.")            # 0입니다.
else :
    print("음수입니다.")

# EX2
score = 87
if score >= 90 :
    print("A")
elif score >= 80 :
    print("B")          # B
elif score >= 70 :
    print("C")
else :
    print("F")

# EX3
num4 = 0
if num4 % 2 == 0 :
    print("짝수입니다.")            # 짝수입니다.
elif num4 % 2 == 1 :
    print("홀수입니다.")
else :
    print("0입니다.")
```

<br>

## input()

- 파이썬에서 사용자 입력을 받는 방법은 input() 합수를 사용
- 문자 입력 받기
  - name = input("이름을 입력하세요")
  - print("안녕하세요", name, "님!")
- 숫자 입력 받기
  - 정수 > int(input("출력문"))
  - 실수 > float(input("출력문"))

```python
# EX1
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

# EX2
A = int(input("첫번째 숫자: "))
B = int(input("두번째 숫자: "))

if A > B :
    print("출력: >")
elif A < B :
    print("출력: <")
elif A == B :
    print("출력: =")

# EX3
id = "korea"
password = 1234

if id == "korea" and password == 1234 :
    print("로그인 되었습니다.")
elif id == "korea" and password != 1234 :
    print("비밀번호가 틀렸습니다.")
else :
    print("회원 가입을 진행해 주세요.")

# EX4
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

# EX5
year = int(input("연도 : "))

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) :
    print("1")
else :
    print("0")
```

<br>

## 반복문이란?

- 여러 줄의 코드 블록을 반복적으로 실행하는데 사용되는 제어 구조
- 반복문을 사용하면 원하는 코드를 원하는 횟수만큼 반복하여 코드를 간결하게 작성하고 효율성을 높일 수 있다.
- for문, while문

### while문

- 반복 횟수를 미리 알 수 없는 경우에 사용
- 조건이 참인 동안 계속해서 코드를 반복한다.
- 조건이 거짓이 될 때까지 반복

```python
# 조건 식이 true(참)이면 아래 들여쓰기가 되어있는 코드가 순차적으로 실행된다.

while 조건식 :
    조건식이 참이면 실행되는 코드

# 무한 루프
while True :
    print("무한 반복한다")
```

```python
# EX1
count = 0
while count < 3 :
    count = count + 1
    print(count)

# Output
1
2
3
```

```python
# EX2
count2 = 0
while count2 < 3 :
    print("안녕하세요!")
    count2 += 1

# Output
안녕하세요!
안녕하세요!
안녕하세요!
```

```python
# EX3
count3 = 9
while count3 > 4 :
    print(count3)
    count3 -= 1

# Output
9
8
7
6
5
```

```python
# EX4
money = 5000
while money >= 3000 :
    print("아이스크림을 사먹었습니다.")
    money -= 1000

# Output
아이스크림을 사먹었습니다.
아이스크림을 사먹었습니다.
아이스크림을 사먹었습니다.
```

```python
# EX5
money2 = 5000
priceOfCandy = 700
numOfCandy = 0

while money2 >= 700:
    money2 -= priceOfCandy
    numOfCandy += 1
    print("사탕을", numOfCandy,  "개 사 먹었습니다.")
print("남은 돈: ", money2, "원")

# Output
사탕을 1 개 사 먹었습니다.
사탕을 2 개 사 먹었습니다.
사탕을 3 개 사 먹었습니다.
사탕을 4 개 사 먹었습니다.
사탕을 5 개 사 먹었습니다.
사탕을 6 개 사 먹었습니다.
사탕을 7 개 사 먹었습니다.
남은 돈:  100 원
```

```python
# EX6. while문을 사용하여 별 찍기
i = 1
while i < 6 :
    print("*" * i)
    i += 1

# Output
*
**
***
****
*****
```

```python
# EX7. while문을 사용하여 별 찍기
i2 = 5
while i2 > 0:
    print("*" * i2)
    i2 -= 1

# Output
*****
****
***
**
*
```

```python
# EX) 구구단
dan = 2
while dan <= 9 :
    n = 1
    while n <= 9 :
        print("{}x{}={}".format(dan, n, dan * n))
        n += 1
    print()
    dan += 1
print("\n")

# Output
2x1=2
2x2=4
2x3=6
~~
9x4=36
9x5=45
9x6=54
9x7=63
9x8=72
9x9=81
```

```python
# EX) 중첩 while문을 사용하여 별찍기
row = 1
while row < 6 :
    star = 1
    while star <= row :
        print("*", end="")
        star += 1
    print()
    row += 1
print()

# Output
*
**
***
****
*****
```

### break와 continue

- break

  - while문을 강제로 종료합니다.
  - while문 내에서 break를 만나면 ,즉시 while문을 벗어나 다음 코드블록으로 이동한다.

    ```python
    # EX1
    while count < 10 :
        print(count)
        count += 1
        if count == 5 :
            break

    # Output
    0
    1
    2
    3
    4
    ```

    ```python
    # EX2
    count2 = 0
    while count2 <= 10 :
        if count2 % 2 == 0 :
            print(count2)
        count2 += 1
    print()

    count3 = 0
    while count3 <= 100 :
        if count3 % 2 == 0 :
            print(count3)
        if count3 == 10 :
            break
        count3 += 1
    print("\n")

    # Output
    0
    2
    4
    6
    8
    10

    0
    2
    4
    6
    8
    10
    ```

- continue

  - while문의 처음 조건으로 이동한다.
  - while문 내에서 continue문을 만나면, 현재 반복을 건너뛰고 그 다음 반복으로 이동한다.

    ```python
    # EX1
    num = 0
    while num < 20 :
        num += 1
        if num % 3 == 0 :
            continue
        print(num, end=" ")     # end = " " 숫자 사이에 띄어쓰기 하나를 추가한다.
                                # end = "," 숫자 사이에 쉼표를 추가

    # Output
    1 2 4 5 7 8 10 11 13 14 16 17 19 20
    ```

    ```python
    # EX2
    num2 = 0
    while num2 < 20 :
       num2 += 1
       if num2 % 3 == 0 :
           print("짝", end = " ")
           continue
       print(num2, end=" ")

    # Output
    1 2 짝 4 5 짝 7 8 짝 10 11 짝 13 14 짝 16 17 짝 19 20
    ```

    ```python
    # EX3. break문과 continue문
    num3 = 0
    while num3 < 20 :
       num3 += 1
       if num3 % 3 == 0 :
           continue
       if num3 == 17 :
           break
       print(num3, end = " ")

    # Output
    1 2 4 5 7 8 10 11 13 14 16
    ```

### for문

- 반복 횟수를 미리 알고 있는 경우에 사용
- 특정 범위 내의 값을 순차적으로 반복하며 코드 블록을 실행한다.

```python
for 변수 in 리스트(목록) :
    실행 코드

# 중첩 for문
for 변수 in 리스트 :
    for 변수 in 리스트 :
        실행 코드
```

```python
# EX1
for n in [1, 2, 3, 4, 5] :
    print(n)

# Output
1
2
3
4
5
```

```python
# EX2
names = ["jennie", "hani", "kelly"]
for name in names :
    print(name)

# Output
jennie
hani
kelly
```

```python
# EX3
for ch in "Hello" :
    print(ch)
print()

for str in "nice" :
    print(str)

# Output
H
e
l
l
o

n
i
c
e
```

```python
# EX4. for문을 활용한 합 구하기
num = [1, 2, 3, 4, 5]
sum = 0

for n in num :
    sum += n
print(sum)

# Output
15
```

```python
# EX5. 리스트 안의 숫자들을 모두 곱해 결과 구하ㄱㅣ
num = [1, 2, 3, 4, 5]
result = 1
for n in num :
    result *= n
print(result)

# Output
120
```

### range 함수

- 시작 숫자부터 리스트를 시작하여 1씩 증가시키면서 종료 숫자 전까지 연속된 리스트를 생성한다.

```python
range(시작 숫자, 종료 숫자)
range(1, 6) 범위 = 1, 2, 3, 4, 5 >> 종료 숫자는 포함 되지 않는다.
range(2, 5) 범위 = 2, 3, 4
```

```python
# EX1
num = range(1, 6)
sum2 = 0
for n in num :
    sum2 += n
print(sum2)         # 15

# EX2. range 함수를 이용해 큰 수 연산하기
sum3 = 0
for n in range(1, 100) :
    sum3 += n
print(sum3)         # 4950
```

### f-string 문자열 포매팅 방식

- 문자열 안에서 중괄호 {}안에 변수를 바로 넣거나, 계산식을 넣어서 결과를 문자열 안에 삽입해주는 역할

```python
# 중첩 for문 예제 1: 2단부터 9단까지 출력하기
for x in range(2, 10) :
    for y in range(1, 10) :
        print(f"{x} X {y} = {x * y}")
    print()
print()

# Output
2 X 1 = 2
2 X 2 = 4
2 X 3 = 6
2 X 4 = 8
~~~
9 X 5 = 45
9 X 6 = 54
9 X 7 = 63
9 X 8 = 72
9 X 9 = 81
```

<br>

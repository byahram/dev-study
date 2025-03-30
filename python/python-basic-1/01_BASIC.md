# [Python1] 기본 개념

<br>

## 기초 문법

### 주석

```python
# 한줄 주석: 메모장 같은 역할 (프로그램 실행에 영향을 주지 않는다.)

"""
여러줄 주석: 큰 따옴표로 감싸서 사용
"""

'''
여러줄 주석: 작은 따옴표로 감싸서 사용
'''
```

### 출력문

```python
print("2025-03-13")
print("Hello World!")
```

### 실행문

- 프로그램이 실제로 동작하면서 각종 작업을 수행하는 코드를 의미한다.
- 즉, 개발자가 컴퓨터에게 내리는 명령이라고 할 수 있다.

<br>

## 변수

### 변수란?

- 필요한 데이터를 메모리라는 임시 저장 공간에 저장한다.
- 임시 저장 공간을 우리는 변수라고 한다. (즉, 데이터를 담아두는 상자)

### 변수 선언하기

- 프로그램에서 변수를 사용하려면 먼저 변수를 저장할 메모리에 공간을 확보해야 한다. (=변수를 선언한다)
- 변수명(상자의 이름표) = 변수값(상자 안에 들어가는 값)
- age = 20

  ```python
  # EX1
  num = 1
  print(num)         # 1

  firstName = 10
  print(firstName)         # 10
  ```

### 변수 이름 짓는 규칙

- 영문, 한글, 숫자 사용 가능
- 대소문자를 구분한다. (num, Num)
- 변수명의 첫 글자는 숫자로 시작할 수 없다.
- 언더바 \_를 제외한 특수문자는 사용할 수 없다(!@^^)
- 파이썬 예약어를 사용할 수 없다.
- 띄어쓰기 불가능

### 카멜 케이스 표기법

- 두단어가 합쳐질 때, 두번째 단어의 첫 글자를 대문자로 작성한다. (firstName)

### 변수 자료형

1. int 정수형

   - 양의 정수 ,음의 정수, 그리고 0을 포함
   - ex) -1, 0, 1, 2, 3...

   ```python
   # EX1
   num1 = 100
   num2 = 300
   print(num1)            # 100
   print(num2)            # 300
   print(num1 + num2)     # 400

   # EX2
   a = 500
   b = 200
   print(a)                # 500
   print(b)                # 200
   print(a * b)            # 100000

   # EX3
   num3 = 100
   num4 = 300
   num5 = num3 + num4
   print(num5)             # 400

   # EX4
   num6 = 500
   num7 = 150
   num8 = num6 - num7
   print(num8)             # 350
   ```

   ```python
   # 변수 값 바꾸는 예제

   # EX1
   num01 = 100
   num02 = 300
   print(num01)      # 100
   print(num02)      # 300

   temp = num01
   num01 = num02
   num02 = temp

   print(num01)      # 300
   print(num02)      # 100

   # EX2
   c = 400
   d = 600

   print(c)          # 400
   print(d)          # 600

   temp2 = c
   c = d
   d = temp2

   print(c)          # 600
   print(d)          # 400
   ```

2. float 실수형

   - 소수와 지수로 구성된 수를 나타내는 자료형
   - ex) 3.14, 3.15

   ```python
   # EX1
   f01 = 30.5
   f02 = 25.3
   print("f01 =", f01)        # f01 = 30.5
   print("f02 =", f02)        # f02 = 25.3

   firstFloat = 3.14
   print("firstFloat =", firstFloat)      # firstFloat = 3.14

   # EX2
   x = 1.7
   y = 2.3
   print(x + y)         # 4.0
   print(x * y)         # 3.9099999999999997
   ```

3. bool 논리형

   - True 혹은 False의 두 가지 값만 가질 수 있다.
   - ex) True(참), False(거짓)

   ```python
   # EX1
   k = 100
   j = 99
   result = k > j
   print(result)        # True

   # EX2
   n01 = 50
   n02 = 75
   result2 = n01 < n02
   print(result2)       # True
   ```

4. String 문자열

   - 텍스트를 표현하는 데 사용되는 자료형
   - 작은 따옴표 '', 큰 따옴표 "", 삼중 따옴표를 사용한다
   - ex) name = "Kim", name = 'Kim'

   ```python
   # EX1
   name = "Kim"
   print(name)          # Kim

   # EX2
   animal = "Cat"
   print(animal)        # Cat

   # EX3. 문자열 합치기
   f_Name = "gildong"
   l_Name = "Hong"
   full_Name = f_Name + l_Name
   print(full_Name)                 # gildongHong

   # EX4. 문자열 반복하기
   hello = "안녕하세요"
   print(hello * 3)                 # 안녕하세요안녕하세요안녕하세요
   ```

<br>

## String 문자열

### 문자열 인덱스

- 문자열의 각 문자는 고유한 번호를 가지며, 이를 인덱스라고 한다.
- 각 문자는 칸이 존재한다.
- 인덱스 번호는 0번부터 시작한다.

```python
# EX1
s = "hello"

f_char = s[0]
t_char = s[2]

print(f_char)     # h
print(t_char)     # l

# EX2
s = "hello"

first_char = s[0]
print(first_char)    # h

last_char = s[-1]
print(last_char)     # o

third_char = s[2]
print(third_char)    # l
print(s[-3])         # l
```

### 문자열 슬라이싱

- 문자열의 일부를 원하는 만틈 잘라내는 기능
- 문법
  - 문자 열을 담은 변수명 [start : stop : step]
  - start(시작 인덱스): 슬라이싱을 시작할 위치를 지정. 생략 가능. 기본 값은 0
  - stop(종료 인덱스): 슬라이싱을 종료할 위치를 지정. 생략 가능. 기본 값은 (마지막 인덱스+1)
  - step(증감폭): 인덱스의 증가 또는 감소 값을 지정. 생략 가능. 기본 값은 1씩 증감.

```python
# EX1
text = "I Love Python"

substring01 = text[2:6]
print(substring01)               # Love

substring02 = text[-6:]          # text[7:13]
print(substring02)               # Python

substring03 = text[7:-1:2]       # text[7:13:2]
print(substring03)               # Pto

substring04 = text[2:6:2]
print(substring04)               # Lv

# EX2
text01 = "I Absolutely Love Python Programming"

substring05 = text01[2:12]
print(substring05)               # Absolutely

substring06 = text01[13:17]
print(substring06)               # Love

substring07 = text01[2:12:2]
print(substring07)               # Asltl
```

### 문자열 길이

- len() 함수 사용
- 문자열의 길이는 공백을 포함한 모든 문자의 개수

```python
# EX1
text03 = "Python"
text03_length = len(text03)
print(text03_length)          # 6

# EX2
text04 = "I Love Python"
text04_length = len(text04)
print(text04_length)          # 13
```

### 문자열 함수

- upper() 함수: 소문자를 대문자로 변환하는 기능
- lower() 함수: 대문자를 소문자로 변환하는 기능

```python
# 소문자 → 대문자 변환 예제
text05 = "i really like computer"

print(text05)                 # i really like computer
text05_upper = text05.upper()
print(text05_upper)           # I REALLY LIKE COMPUTER

# 대문자 ↔ 소문자 변환 예제
text06 = "I Don't really Like TO Reading book"

print(text06)                 # I Don't really Like TO Reading book
text06_upper = text06.upper()
text06_lower = text06.lower()
print(text06_upper)           # I DON'T REALLY LIKE TO READING BOOK
print(text06_lower)           # i don't really like to reading book
```

<br>

## 연산자

- 수학적 계산과 데이터 처리를 수행하기 위해 사용하는 기호 또는 기호 조합을 의미.

### 파이썬에서 지원하는 연산자 종류

- 산술 연산자: +, -, \*, /, %, //, \*\*
- 대입 연산자: =, +=, -=, \*=, /=
- 비교 연산자: ==, !=, >, <, >=, <=
- 논리 연산자: not, and, or
- 부호 연산자: -

### 파이썬에는 없는 연산자

- ++(증가 연산자), --(감소 연산자)

### 산술 연산자

- // 나눗셈 몫: a//b a를 b로 나눈 몫
- % 나눗셈 나머지: a&b a를 b로 나눈 나머지
- ** 거듭 제곰: a**b a를 b로 제곱한 결과
- c/c++/java: 나눗셈 몫, 거듭 제곱을 사용하지 않음.

```python
# EX1
num01 = 10
num02 = 2

print(num01 + num02)        # 더하기(+): 12
print(num01 - num02)        # 빼기(-): 8
print(num01 * num02)        # 곱하기(*): 20
print(num01 / num02)        # 나누기(/): 5.0
print(num01 % num02)        # 나머지(%): 0
print(num01 // num02)       # 몫 구하기(//): 5
print(num01 ** num02)       # 거듭 제곱 연산자(**) = 10을 2번 곱해라: 100

# EX2
num03 = 15
num04 = 4

print(num03 + num04)        # 더하기: 19
print(num03 - num04)        # 빼기: 11
print(num03 * num04)        # 곱하기: 60
print(num03 / num04)        # 나누기: 3.75
print(num03 % num04)        # 나머지: 3
print(num03 // num04)       # 몫 구하기: 3
print(num03 ** num04)       # 거듭 제곱: 50625
```

### 대입 연산자

- 변수에 값을 할당하는 데 사용하는 연산자
- =

```python
# EX1
num05 = 77
num06 = 23
num05 = num05 + 23
num06 = num06 - 3

print(num05)         # 100
print(num06)         # 20

num05 = 77
num06 = 23
num05 += 23
num06 -= 3

print(num05)         # 100
print(num06)         # 20
```

### 복합 대입 연산자

- 코드가 간결하다
- 피연산자 : 연산의 대상이 되는 숫자, 변수, 또는 값 자체를 의지
  - ex) a + b = a와 b가 피연산자
  - ex) 10 + 5 = 10, 5가 피연산자
- += : 왼쪽 피연산자에 오른쪽 피연산자를 더한 결과 값을 대입
- -= : 뺀 결과 값을 대입
- \*= : 곱한 결과 값을 대입
- /= : 나눈 결과 값을 대입
- //= : 나눈 몫을 대입
- %= : 나머지 값을 대입

```python
# EX1
num07 = 66
num08 = 13
num09 = num07 + num08
num07 += num08
num09 -= num07

print(num07)         # 79
print(num08)         # 13
print(num09)         # 0

# EX2
num1 = 7
num2 = 3
num3 = num1 // num2
num1 += num2
num3 *= num2

print(num1)          # 10
print(num2)          # 3
print(num3)          # 6
```

### 비교 연산자

- 두 개의 값을 비교하여 그 결과가 참(true)인지 거짓(false)인지 판별 하는 연산자로, 관계 연산자 라고도 한다.
- 수학적인 부등호처럼 두 값의 관계를 판단 하는 역할.
- \> 크다
- < 작다
- \>= 크거자 같다
- <= 작거나 같다
- == 같다
- != 같지 않다

```python
# EX1
a = 70
b = 60

a_is_bigger = a > b
a_is_smaller = a < b
is_equal = a == b
is_not_equal = a != b

print(a_is_bigger)         # True
print(a_is_smaller)        # False
print(is_equal)            # False
print(is_not_equal)        # True

# EX2
str1 = "abc"
str2 = "a" + "b" + "c"

is_equal2 = (str1 == str2)
print(is_equal2)           # True

one = "1"
num = 1

is_not_equal = (one != num)
print(is_not_equal)        # True
```

### 논리 연산자

- 논리적인 연산을 수행하여 참인지 거짓인지를 판단하는 연산자
- and: 연산자를 기준으로 왼쪽과 오른쪽 값이 모두 true 일때만 true를 반환, 나머지는 모두 false (&&, &: 다른 언어)
- or: 연산자를 기준으로 왼쪽과 오른쪽 값이 하나라도 true면 true를 반환, 둘다 false일때만 false 반환 (||: 다른 언어)
- not: 뒤에 따라오는 논리값이 true이면 false를 반환, false이면 true를 반환 (!: 다른 언어)

```python
# EX1
is_snowing = True
is_cold = True
is_winter = (is_snowing and is_cold)
print(is_winter)        # True

# EX2
is_snowing2 = 1
is_cold2 = 0
is_winter2 = is_snowing2 & is_cold2
print(is_winter2)       # 0

# EX3
is_raining = 1
is_windy = 0
print(is_raining & is_windy)        # 0

# EX4. not
is_false = False
print(not is_false)        # True

is_true = True
print(not is_true)         # False
```

### 부호 연산자

- 숫자 앞에 - 부호를 붙여 양수를 음수로, 음수를 양수로 변환할 수 있다.
- 즉, 숫자의 부호를 변경한다.
- ex) x = 10, x = -x, x = -10

```python
# EX1
x = 10
x = -x
print(x)       # -10

# EX2
x = -x
print(x)       # 10

# EX3
is_true = True
print(- is_true)        # -1
```

<br>

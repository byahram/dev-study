"""
2025.04.10 화
"""

print()
print()
print("------------------------")
print("--- 에러와 예외")
print("------------------------")
print()

"""
[에러] : 프로그래밍 도중 발생하는 문제
        - 아예 실행 자체가 되지 않는 것
        - ex) 괄호 빼먹음, 들여쓰기 오류
        
[예외] : 문법은 맞지만, 실행 도중 발생하는 오류
        - 코드는 실행 되지만 중간에 멈추는 것
        - 0으로 나누기, 없는 파일 열기 등

[예외 클래스 12가지 예외 클래스]

1. 최상위 예외 클래스 : BaseException
2. 대부분 예외 클래스의 슈퍼 클래스 : Exception
3. 산술 연산 오류 : ArithmeticError
4. 잘못된 속성 참조 : AttributeError
5. 파일에서 더 이상 읽을 데이터가 없음 : EOError
6. import할 모듈이 없을 때 : ModuleNotFoundError
7. 존재하지 않은 파일 : FileNotFoundError
8. 잘못된 인덱스 사용 : IndexError
9. 잘못된 이름(변수) 사용 : NameError
10. 문법 오류 : SyntaxError
11. 계산하려는 데이터의 유형 오류 : TypeError
12. 계산하려는 데이터의 값 오류 : ValueError 
"""

# EX1.
# 사용자 입력 기반 나눗셈
num1 = int(input("첫번째 정수를 입력하세요 >> "))
num2 = int(input("두번째 정수를 입력하세요 >> "))

if num2 == 0 :
    print("0으로 나눌수 없습니다.")
else :
    print("num1 / num2 =", num1 / num2)

print()
print("------------------------")
print()

# EX2.
fruits = ["사과", "바나나", "포도", "딸기"]
print("fruits 리스트 출력 :", fruits)

idx = int(input("몇번째 과일이 보고 싶습니까? (0부터 시작) >> "))
if idx < len(fruits) :
    print(f"{idx}. {fruits[idx]}")
else :
    print("리스트 범위가 벗어납니다.")

print()
print()
print("------------------------")
print("--- try-except")
print("------------------------")
print()

'''
[try-except]

: 예외 상황을 처리하는데 가장 기본적으로 사용되는 구문이다.

[문법]

try :
    # 예외가 발생할 수 있는 코드 블록
except:
    # 예외가 발생했을 떄 수행되는 코드 블록
    
[예외에 따라 메시지를 변경하는 기본 형태]

try :
    # 예외가 발생할 수 있는 코드 블록
except [발생 예외1] :
    [발생 예외1]에 해당하면 수행되는 코드 블록
except [발생 예외2] :
    [발생 예외2]에 해당하면 수행되는 코드 블록
'''

# EX1.
try :
    num1 = int(input("첫번째 정수를 입력하세요 >> "))
    num2 = int(input("두번째 정수를 입력하세요 >> "))
    print("num1 / num2 =", num1 / num2)

except :
    print("예외가 발생했습니다.")

print()
print("------------------------")
print()

# EX2.
try :
    age = int(input("나이를 입력해 주세요. >> "))
    print("입력된 나이", age)
except :
    print("예외가 발생했습니다.")

print()
print("------------------------")
print()

# EX3. 사용자 입력 숫자만큼 반복 출력 예제
try :
    count = int(input("숫자를 입력하세요. >> "))

    for i in range(0, count) :
        print(f"{i + 1}번째 : 안녕하세요!")
except:
    print("정수가 아닙니다.")

print()
print("------------------------")
print()

# EX4.
try :
    num1 = int(input("첫번째 정수를 입력하세요 >> "))
    num2 = int(input("두번째 정수를 입력하세요 >> "))
    print("num1 / num2 =", num1 / num2)

# 산술 연산 예외 처리 클래스
except ArithmeticError:
    print("산술 연산 예외가 발생했습니다.")

# 입력값 예외
except ValueError :
    print("입력값 예외가 발생했습니다.")

print()
print("------------------------")
print()

# EX5.
fruitsList = ["체리", "바나나", "딸기", "블루베리"]
try :
    idx = int(input("인덱스 값을 입력하세요. >> "))
    print(f"{idx}. {fruitsList[idx]}")

except IndexError :
    print("인덱스 범위를 벗어났습니다.")

except ValueError :
    print("입력값 예외가 발생했습니다.")

print()
print()
print("------------------------")
print("--- try-except, as")
print("------------------------")
print()

'''
[try-except[발생 예외] as 예외 메시지 변수]

- 예외가 발생했을 때 그 메시지를 변수에 담아 활용하고 싶을 때 사용한다.

[문법 ]

try :
    # 예외가 발생할 가능성이 있는 코드
except 예외 클래스 as 변수 :
    # 예외 메시지를 변수로 받아서 처리하는 코드

[언제 쓰면 좋을까?]

- 로그 기록할 때
- 사용자에게 더 정확한 피드백을 줄때
- 디버깅용으로 예외 메시지를 확인하고 싶을떄
'''

# EX1. as절을 사용하여 예외 메시지 출력하기
try :
    num1 = int(input("첫번째 정수를 입력하세요 >> "))
    num2 = int(input("두번째 정수를 입력하세요 >> "))
    print("num1 / num2 =", num1 / num2)

except ArithmeticError as e:        # e 변수에 예외 객체를 저장
    print("산술 연산 예외가 발생했습니다.")
    print(e)

except ValueError as e :
    print("입력값 예외가 발생했습니다.")
    print(e)

print()
print("------------------------")
print()

# EX2.
try :
    age = int(input("나이를 입력해 주세요. >> "))
    print("입력된 나이", age)

except ValueError as e :
    print("입력값 예외가 발생했습니다.")
    print("Error :", e)
    
print()
print("------------------------")
print()

# EX3.
carList = ["현대", "기아", "테슬라", "BMW"]
try :
    idx = int(input("인덱스를 입력해 주세요. >> "))
    print(f"{idx}. {carList[idx]}")
    
except IndexError as e :
    print("인덱스를 벗어났습니다.")
    
except ValueError as e :
    print("입력값 예외가 발생했습니다.")

print()
print()
print("------------------------")
print("--- try-finally, else")
print("------------------------")
print()

'''
[try-finally, else]

- finally : try 블록에서 예외 발생 여부와 상관없이 항상 실행되는 코드
'''

# EX1.
try :
    list = [1, 2, 3, 4]
    print(list[5])  # 예외 발생 시점
    print("try 구문 안에 예외 발생 후 코드")

except IndexError as e :
    print(e)

finally :       # 예외 발생과 상관없이 항상 실행되는 코드 블록
    print("안녕하세요")
    
print()
print("------------------------")
print()

'''
[KeyError] 

: 딕셔너리에 존재하지 않는 "키(key)를 사용해서 값을 꺼내려고 할때 발생하는 예외"

[KeyError 자주 발생할 때]

1. 사용자 입력으로 키를 받을 때
2. API 응답에서 특정 키를 기대할 때
3. 반복문이나 조건문 없이 바로 키 접근할 때
'''

# EX2.
try :
    dic = {
        "name" : "지훈",
        "age" : 20,
    }

    # 예외 발생
    print(dic["grade"])
    print("이 줄은 실행되지 않아요")

except KeyError as e :
    print("Error :", e)

finally :
    print("프로그램을 종료합니다.")

print()
print()
print("------------------------")
print("--- try-except-else")
print("------------------------")
print()

'''
[try-except-else 문법]
try :
except :
else :  
    # 정상적으로 실행되면 수행되는 코드 블록
    
[언제 쓰면 좋을까?]

- try 안에서 오류가 없을 때만
- 실행할 후속 처리가 필요할 때
- try 에는 위험한 코드만, else에는 안전한 코드만
'''

# EX1
try :
    num = int(input("숫자 입력해주세요 >> "))
except ValueError :
    print("숫자 아닌 값을 입력했습니다.")
else :
    print(f"입력한 숫자는 {num}입니다")

print()
print("------------------------")
print()

# EX2
try :
    num = int(input("좋아하는 숫자를 입력하세요 >> "))
except ValueError as e:
    print("숫자 아닌 값을 입력했습니다.")
    print("Error :", e)
else :
    if num > 0 :
        print("양수를 좋아하시는군요")
    elif num == 0 :
        print("0을 좋아하시는구요")
    else :
        print("음수를 좋아하시는군요")

print()
print()
print("------------------------")
print("--- 커스텀 예외 클래스")
print("------------------------")
print()

'''
[커스텀 예외 클래스]

- 강제로 예외 발생 시키는 raise
 (= 프로그래머가 직접 예외를 발생시키기 위해 사용하는 키워드)
- 기본적으로  try 블록 안에서 쓰이며, 원하는 조건일 때 일부러 에러를 만들고 그 에러를 처리하도록 할 수 있다.

[문법]

- raise 예외 클래스("예외 메시지")
- 이 코드를 만나면 즉시 예외가 발생하고, 프로그램이 멈추거나 except로 넘어감

[언제 쓸까?]
사용자 입력 검증                나이가 0보다 작을 수 없을 떄
함수 내부 조건 체크             파라미터(매개변수)가 비어있을때
사용자 정의 예외와 함께 사용     직접 만든 예외 클래스와 raise
'''

# EX1. 조건에 따라 예외 발생
try :
    age = int(input("나이를 입력하세요 >> "))
    if age < 0:
        raise ValueError("나이는 음수가 될 수 없다.")
except ValueError as e :
    print("예외 발생 :", e)
else :
    print("입력한 나이는 :", age)

print()
print("------------------------")
print()

# EX2. 몸무게 입력 검사
try :
    weight = int(input("몸무게를 입력하세요 >> "))
    if weight < 0 :
        raise ValueError("0 이하입니다.")
    
except ValueError as e :
    print("예외 발생 :", e)

else :
    print(f"입력한 몸무게는 {weight}kg 입니다.")

print()
print()
print("------------------------------")
print("--- 사용자 정의 예외 클래스")
print("------------------------------")
print()

'''
[사용자 정의 예외 클래스]

개발자가 직접 만든 상황에 맞는 예외를 정의하여 사용할 수 있다.
기본 제공되는 예외(ValueError, IndexError 등) 외에..

[문법]

class 예외이름(Exception) :      #  Exception 클래스를 상속해서 새 예외 클래스를 만든다.
    pass                        # 내용이 없어도 클래스 정읳를 허용해주는 예약어
    
[사용자 정의 예외가 좋은 경우]

1. 예외를 더 구체적이고 의미있게 표현할 수 있다.
2. 큰 프로젝트에서 특정 상황만을 따로 처리할 수 있다.
3. 가독성관 유지보수가 좋다.

[사용자 정의 예외 클래스에 __init__()]

- 사용자 정의 예외 클래스에 __init__()을 추가해서 메시지를 커스터마이징할 수 있다.
1. 왜 __init__()을 직접 정의할까?
2. 에러 메시지를 더 유연하게 처리할 수 있다.
3. 예외 객체 안에 추가 데이터도 담을 수 있다.

[문법 구조]

class 사용자정의예외(Exception) :
    def __init__(self, 메시지)
        self.message = 메시지      # 예외 객체에 메시지 저장
        super().__init__(self.message)      # 부모 클래스 Exception에세 메시지 전달
'''

# EX1. 나이가 너무 적을 때 예외 발생시키기
# 사용자 정의 예외 클래스 만들기

class TooYoungError(Exception) :
    pass

try :
    age = int(input("나이를 입력하세요 >> "))
    if age < 10 :
        raise TooYoungError("10세 미만은 사용할 수 없습니다.")
    
except TooYoungError as e :
    print("사용자 정의 예외 발생 :", e)

except ValueError as e :
    print("Error :", e)

print()
print("------------------------")
print()

'''
[message를 쓸 수 있는 이유?]

- Exception 클래스의 __init__() 메서드에는 message라는 이름의 매개변수는 없지만 *org로 받아서 메시지를 처리해주기 때문이다.
- args는 "개수가 정해지지 않은 여러 개의 인자(값)"를 함수에 전달할 떄 사용하는 문자
'''

# EX2.
class TooLowScoreError(Exception) :
    def __init__(self, score):
        self.score = score
        self.message = f"점수가 너무 낮습니다. : {score}점 (최소 60점 필요)"
        super().__init__(self.message)

try :
    score = int(input("정수를 입력하세요 >> "))
    if score < 60 :
        raise TooLowScoreError(score)

except TooLowScoreError as e :
    print("사용자 정의 예외 발생 :", e)

print()
print()
print("------------------------ 끝")
print()
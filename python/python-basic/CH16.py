"""
2025.04.24 목
"""

print()
print()
print("------------------------")
print("--- 자료 구조")
print("------------------------")
print()

'''
[자료 구조]

- 컴퓨터 프로그램 안에서 데이터를 체계적으로 저장하고, 관리하는 방식이다.
- 자료구조는 데이터를 '효율적'으로 저장하고 관리하기 위한 구조화된 방식이다.
- "데이터를 어떻게 구조화 할 것인가"에 대한 고민

[왜 필요한가?]

- 프로그래밍에서 다루는 거의 모든 문제는 "데이터를 처리하는 문제"이다.
- 데이터를 무작정 저장하면, 원하는 정보를 찾는데 시간이 오래걸리거나, 추가/삭제 작업이 복잡해진다.

[예시]

- 고객 정보를 저장하고 검색해야한다.
- 수강 신청 내역을 빠르게 불러와야한다.
- 게임에서 수천 개의 오브젝트를 실시간으로 처리해야한다.
-> 데이터를 효율적으로 저장, 탐색, 수정, 삭제하기 위해 자료구조가 반드시 필요하다.

[자료구조가 중요한 세가지 이유]

1. 속도
    - 좋은 자료구조를 사용하면 프로그램의 실행 속도가 크게 향상된다.
    - 빅오(Big-O) 표기법 : "이 코드(또는 알고리즘)는 얼마나 효율적일까?"를 수학적으로 표현하는 방법
2. 유지보수
3. 현실 문제 해결

[빅오(Big-O) 표기법]

빅오표기         의미              예시                               비유                                                정확한 의미 
O(1)          상수시간          리스트[0]                         1층 버튼 바로 누르기                                      바로 접근 가능
O(log n)      로그시간          이진 탐색                         몇 층인지 모르지만, 중간부터 시작해서 절반씩 범위 줄이기       절반씩 탐색(이진 탐색 구조)                                               
O(n)          선형시간          for 반복문 : 데이터 개수에 비례      계단을 하나씩 내려가기                                    모든 데이터를 다 봐야한다
O(n log n)    로그선형          효율적인 정렬                         
O(n^2)        제곱시간          중첩반복문                         건물 사람 전부 만나서 인사                                모든 조합 다 탐색
O(2^n)        지수시간          피보나치 재귀(비효율적)
O(n!)         팩토리얼 시간      순열 탐색

* O(n log n) -> 자주 쓰임 : 정렬 알고리즘 (퀵 정렬, 병합 정렬), 일부 탐색 알고리즘
'''

print("--------------------------------------")
print("--- 1. 배열(array): array.array")
print("--------------------------------------")
print()

'''
[1. 배열(array)]

- 대표적으로 두가지 : array.array, numpy.array

[array.array]

- 기본 제공 배열 모듈
- 같은 자료형만 저장 가능한 1차원 배열
- 메모리를 덜 쓰고, 리스트보다 약간 빠름
- 하지만 기능이 매우 제한적 -> 실무에서는 거의 사용되지 않음
- 저장공간이 제한되어 있음
- 잘 저장한다.

[어디서 쓰이나요?]

- 간단한 센서 데이터 저장, 파일 I/O 처리 등

[array() 함수의 구조]

array(typecode, initializer)

- typecode : 배열에 저장할 데이터의 자료형을 지정하는 한 글자 코드
- initializer : 초기데이터(보통 리스트)

[실무 및 학습에서 자주 사용하는  type코드 4가지]

타입코드    : 타입   : 설명                   : 주 사용 용도
"i"        : int   : 4byte 정수             : 일반적인 정수 저장용
"f"        : float : 4byte 실수             : 소수점 포함된 숫자 저장용
"d"        : float : 8byte 실수(double)     : 더 높은 정밀도의 실수 계산용
"B"        : int   : 1byte 양의 정수(0~255)  : 바이트 데이터

[리스트와 배열의 차이점(용어 설명)]

- list(리스트) : 파이썬에서 기본적으로 제공하는 자료형, 여러 타입 가능
- array.array : 파이썬 표준 모듈, 같은 타입만 저장
- numpy.array : 외부라이브러리, 고성능 수치 연산용

항목        :   list                :   array               :   numpy.array
제공방식     :  기본자료형            :    표준모듈(import)     :   외부라이브러리
저장 자료형  :  자유                  :   하나                 :   하나
차원        :  기본은1차원(다차원 중첨) :   1차원               :   1차원~n차원               
수학 연산    :  직접 구현              :   불편                :   함수로 연산 가능
속도        :  느림                  :    약간 빠름            :    매우 빠른(C)
사용 빈도    :  매우 높음              :   거의 안씀            :   데이터 처리에서 표준
'''

from array import array

# 배열 array.array 예제 1

# 일반적인 정수 저장
arr = array('i', [1, 2, 3, 4, 5])           # 동일한 타입의 숫자만 다룰때
print(arr)

# 일반적인 소수(실수) 저장
f_arr = array("f", [1.5, 2.5, 3.5, 4.5])        # 부동 소수점 약 7자리 정확도
print(f_arr)

# 더 정밀한 실수 계산이 필요할 때
d_arr = array("d", [3.14151416171781])          # 약 15~17자리 유효 숫자의 정밀도를 가진다.
print(d_arr)

# 0~255 범위의 바이트 저장
b_arr = array("B", [0, 155, 255])
print(b_arr)

print()
print()
print("------------------------")
print("--- Numpy")
print("------------------------")
print()

'''
[Numpy의 정의]

- Numerical Python의 줄임말
- 수치

[특징]

- 다차원 배열 객체인 numpy.array 제공
- 내부는 C언어로 구현되어 있어서 빠르다
- 반복문 없이 배열 전체에 연산 가능(-> 벡터화 연산)
- 선형대수, 통계 난수 생성등 과학 계산 기능 포함

[1, 2, 3, 4] -> 1차원 배열
[1, 2, 3, 4
 1, 2, 3, 4] -> 2행(가로줄) 4열(세로줄)의 다차원 배열

[왜 중요한가?]

- 리스트보다 훨씬 빠르고, 효율적이며, 확장성 있는 수치 처리가 가능하다.
- 데이터분석, 머신러닝, 영상처리, 공학 계산등에서 사실상 표준 도구로 사용된다.
'''

'''
[as]

- as는 별칭을 지정하는 키워드
- 넘파이를 np라는 이름을 불러오겠다

[as 왜 사용할까?]

1. 코드를 짧고 간결하게 쓰려고
2. 관례(대부분의 파이썬 개발자들은 넘파이를 np로 쓴다)
'''
import numpy as np

# 예제 1. 1차 배열
a = np.array([1,2,3])
print(a * 2)
print()

arr = array("i", [10, 20, 30])
print("배열 :", arr)
print("배열 * 2 :", arr * 2)

print()
print("------------------------")
print()

# 예제 2. 2차 배열
arr2d = np.array([[1, 2, 3], [4, 5, 6]])      # 2차원 배열
result1 = arr2d + 100       # 모든 요소에 100을 더하기

print("원본 배열 : \n", arr2d)
print()
print("100을 더한 배열 : \n", result1)

print()
print("------------------------")
print()

'''
[브로드캐스팅]

- 1차원 배열을 각 행에 더함
->  numpy의 핵심 기능 중 하나로, 서로 다른 크기의 배열 간 연산을 자동으로 맞춰주는 기능이다

[예외]

# a = np.array([[1, 2], [3, 4]])    2행 2열
# b = np.array([1, 2, 3])       1행 3열
# 차원이 안 맞아서 브로드캐스팅 불가능
'''

# 예제 3. 2차 배열
arr2d = np.array([[10, 20, 30],[40, 50, 60]])           # 2차 배열
arr1d = array("i", [1, 2, 3])         # 1차원 배열
ressult = arr2d + arr1d

print("2차원 배열 :\n", arr2d)
print()
print("1차원 배열 :\n", arr1d)
print()
print("덧셈한 배열 :\n", ressult)

print()
print()
print("------------------------")
print("--- Numpy 함수")
print("------------------------")
print()

'''
[Numpy에서 자주 사용하는 통계 함수 정리]

- np.sum()                  총합 계산
- np.mean()                 평균 계산
- np.median()               중앙값 계산
- np.std()                  표준 편차 계산
- np.var()                  분산 계산
- np.min/max()              최대/최소
- np.argmax/argmin()        최대, 최소값의 인덱스

[문법]

문법 np.원하는 연산 함수(연산할 배열 이름)
'''

# 예제 1
scores = np.array([85, 90, 78, 92, 88])

print("합계 :", np.sum(scores))
print("평균 :", np.mean(scores))
print("중앙값 :", np.median(scores))
print("표준편차 :", np.std(scores))
print("분산 :", np.var(scores))
print("최소 :", np.min(scores))
print("최대 :", np.max(scores))
print("최대 인덱스 :", np.argmax(scores))
print("최소 인덱스 :", np.argmin(scores))

print()
print()
print("------------------------")
print("--- 상관 계수")
print("------------------------")
print()

'''
[상관 계수]
- np.corrcoef(arr1, arr2)
- 두 배열 간의 상관 관계(얼마나 같이 오르내리는지)를 계산
- 상관계수 1은 완벽한 양의 상관관계를 뜻한다.
- 반환값 : 2차원 행렬 형태의 상관계수
- 값 번위 : -1~1
    : 해석) 1 완벽히 같이 움직임, 0 무관, -1 반대로 움직임
'''

# 상관 계수 예제
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

corr_m = np.corrcoef(x, y)
print(corr_m)

print()
print()
print("------------------------------")
print("--- 연결리스트(LinkedList)")
print("------------------------------")
print()

'''
[연결 리스트(Linked List)]

- 연결 리스트는 데이터를 차례대로 연결해 저장하는 구조이다.
- 각 데이터는 단순히 저장되는 것이 아니라, 자기 자신 + 다음 데이터를 가리키는 주소를 함께 갖고 있다.
- 포인터 : 메모리 주소를 저장하는 변수

[연결 리스트가 실생활에서 쓰이는 곳]

1. 웹 브라우저의 "뒤로가기/앞으로가기"
    [네이버] -> [구글] -> [다음]
2. 음악 재생 플레이 리스트

[단일 연결 리스트(Single Linked List)]

- 단일 연결 리스트는 한 방향으로만 연결되어 있는 가장 기본적인 형태의 연결 리스트다.
- [data | 주소] -> [data | 주소] -> [data | 주소]
- [체리 | 바나나 노드 주소] -> [바나나 | 수박의 노드 주소] -> [수박 | None]

[Node(노드)란?]

- 연결 리스트에서 하나의 데이터 단위를 의미한다.
- [data | 포인터(다음 노드의 주소)]
- data : 저장할 실제 값
- 포인터 : 다음 노드의 주소

[Node(노드) 예시]

- 리스트 : [1, 2, 3, 4]
- [1 | 2의 주소값] -> [2 | 3의 주소값] -> [3 | 4의 주소값] -> [4 | None]

[연결 리스트의 주요 장점]

1. 크기 제한 없음(동적 메모리 할당)
2. 삽입 | 삭제가 빠르다.
3. 메모리 효율적
4. 스택, 뮤 등 다양한 자료구조 구현에 유리하다.

[언제 사용할까?]

1. 데이터 양이 자주 바뀌는 경우
2. 중간 삽입/삭제가 자주 필요한 경우
3. 메모리 공간을 연속적으로 확보하기 힘든 경우
'''

# Node 클래스 예제 1
# [데이터 | 빈주소]
class Node :
    def __init__(self, data):
        # 노드가 저장하는 데이터
        self.data = data
        # 다음 노드를 가리키는 포인터
        self.next = None

# 노드 생성
node1 = Node(10)      # 노드만 생성
node2 = Node(20)      # 노드만 생성

# node1 -> node2를 연결
node1.next = node2

# 출력
print("node1의 값 :", node1.data)
print()
print("node1이 가리키는 node2의 값 :", node1.next.data)

print()
print("------------------------")
print()

# Node 클래스 예제 2
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

n1 = Node(100)
n2 = Node(200)
n3 = Node(300)

n1.next = n2
n2.next = n3

print("n1의 값 :", n1.data)
print("n2의 값 :", n2.data)
print("n3의 값 :", n3.data)

print(id(n1))
print(id(n2))
print(id(n3))

print()
print("------------------------")
print()

'''
[헤드란?]

['체리', '바나나', '수박']
head -> [체리 | 바나나의 주소] ->

- 연결 리스트의 시작점을 가리키는 포인터이다.
- 즉, 첫번째 노드를 가리키는 변수

-> 우리가 연결리스트를 탐색할 떄는 항상 head부터 출발
-> head가 없다면 연결리스트 전체를 알 수 없다.
'''

# # Node 클래스 예제 3
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

f1 = Node("체리")
f2 = Node("바나나")
f3 = Node("수박")

f1.next = f2
f2.next = f3

# head 설정
head = f1

# 출력
current = head

while current : 
    print(current.data)
    current = current.next

print()
print()
print("------------------------------------")
print("--- 연결리스트(LinkedList): 삽입")
print("------------------------------------")
print()

'''
[LinkedList에서 삽입(insert)이란?]

- 연결 리스트의 원하는 위치에 새로운 노드를 추가하여 기존 노드들과 포인터로 연결하는 동작을 말한다.
- 연결 리스트는 연속된 메모리가 필요 없기 때문에, 중간이든 앞이든 뒤든 어디든지 삽입이 가능하다.

[이전 노드] -> [다음 노드]
[이전 노드] -> [새 노드 ] -> [다음노드]
'''

# Node 클래스 삽입 예제
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

f1 = Node("체리")
f2 = Node("바나나")
f3 = Node("수박")

f1.next = f2
f2.next = f3

# head 설정
head = f1

# 1.1. 맨 앞에 노드 삽입(딸기)
# 딸기 체리 바나나 수박
new_node = Node("딸기")
new_node.next = head        # 기존 리스트의 head를 new_node가 가리킴
head = new_node             # head를 new_node로 갱신(renewal)

# 1.2. 맨 앞 노드 삽입(블루베리)
# 블루베리 딸기 체리 바나나 수박
new_node2 = Node("블루베리")
new_node2.next = head
head = new_node2

# 2.1. 중간 노드 삽입(오렌지)
# 블루베리 딸기 체리 바나나 오렌지 수박
new_node3 = Node("오렌지")
target = f2                     # target은 바나나 노드
new_node3.next = target.next    # 오렌지가 수박을 가리킴
                                # 오렌지의 주소 = 수박 주소
target.next = new_node3

# 2.2 중간 노드 삽입(사과)
# 블루베리 딸기 사과 체리 바나나 오렌지 수박
new_node4 = Node("사과")
target = head.next                  # head는 블루베리 -> head.next는 딸기
new_node4.next = target.next        # 사과가 체리를 가리킴
target.next = new_node4             # 딸기가 사과를 가리킴

# 출력
current = head

while current : 
    print(current.data)
    current = current.next

print()
print()
print("------------------------ 끝")
print()
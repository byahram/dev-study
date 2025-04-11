"""
2025.03.21 금
"""

print()
print()
print("------------------------")
print("--- break문")
print("------------------------")
print()

'''
[break]

- while문을 강제로 종료합니다.
- while문 내에서 break를 만나면 ,즉시 while문을 벗어나 다음 코드블록으로 이동한다.
'''

# break문 예제 1
count = 0
while count < 10 :
    print(count)
    count += 1
    if count == 5 :
        break

print()
print("------------------------")
print()

# 예제 2
count2 = 0
while count2 <= 10 :
    if count2 % 2 == 0 :
        print(count2)
    count2 += 1

print()
print("------------------------")
print()

count3 = 0
while count3 <= 100 :
    if count3 % 2 == 0 :
        print(count3)
    if count3 == 10 :
        break
    count3 += 1

print()
print()
print("------------------------")
print("--- continue문")
print("------------------------")
print()

'''
[continue]

- while문의 처음 조건으로 이동한다.
- while문 내에서 continue문을 만나면, 현재 반복을 건너뛰고 그 다음 반복으로 이동한다.
'''

# 예제 1
num = 0
while num < 20 :
    num += 1
    if num % 3 == 0 :
        continue
    print(num, end=" ")     # end = " " 숫자 사이에 띄어쓰기 하나를 추가한다. 
                            # end = "," 숫자 사이에 쉼표를 추가

print()
print("------------------------")
print()

# 예제 2
num2 = 0
while num2 < 20 :
    num2 += 1
    if num2 % 3 == 0 :
        print("짝", end = " ")
        continue
    print(num2, end=" ")
print("\n")

print()
print("-----------------------------")
print("--- break문과 continue문")
print("-----------------------------")
print()

# 예제 1
num3 = 0
while num3 < 20 :
    num3 += 1
    if num3 % 3 == 0 :
        continue
    if num3 == 17 :
        break
    print(num3, end = " ")
print("\n")

print()
print("-----------------------------")
print("--- while을 이용한 구구단")
print("-----------------------------")
print()

dan = 2
while dan <= 9 :
    n = 1
    while n <= 9 :
        print("{}x{}={}".format(dan, n, dan * n))
        n += 1
    print()
    dan += 1
print("\n")

print("----------------------------------")
print("--- 중첩 while을 이용한 별찍기")
print("----------------------------------")
print()

row = 1
while row < 6 :
    star = 1
    while star <= row :
        print("*", end="")
        star += 1
    print()
    row += 1

print()
print()
print("-----------------------------")
print("--- for문")
print("-----------------------------")
print()

'''
[for문]

- 반복 횟수를 미리 알고 있는 경우에 사용
- 특정 범위 내의 값을 순차적으로 반복하며 코드 블록을 실행한다.

# 문법
for 변수 in 리스트(목록) :
    실행 코드

# 중첩 for문
for 변수 in 리스트 :
    for 변수 in 리스트 :
        실행 코드
'''

# 예제 1
for n in [1, 2, 3, 4, 5] :
    print(n)

print()
print("------------------------")
print()

# 예제 2
names = ["jennie", "hani", "kelly"]
for name in names :
    print(name)

print()
print("------------------------")
print()

# 예제 3
for ch in "Hello" :
    print(ch)
print()

for str in "nice" :
    print(str)

print()
print("------------------------")
print()

# 예제 4. for문을 활용한 합 구하기 예제
nums = [1, 2, 3, 4, 5]
sum = 0
for n in nums :
    sum += n
print(sum)

print()
print("------------------------")
print()

# 예제 5. 리스트 안의 숫자들을 모두 곱해 결과 구하는 예제
nums2 = [1, 2, 3, 4, 5]
result = 1
for n in nums2 :
    result *= n
print(result)

print()
print()
print("------------------------")
print("--- range()")
print("------------------------")
print()

'''
[range()]

- 시작 숫자부터 리스트를 시작하여 1씩 증가시키면서 종료 숫자 전까지 연속된 리스트를 생성한다.

range(시작 숫자, 종료 숫자)
range(1, 6) 범위 = 1, 2, 3, 4, 5 >> 종료 숫자는 포함 되지 않는다.
range(2, 5) 범위 = 2, 3, 4
'''

# 예제 1
nums3 = range(1, 6)
sum2 = 0
for n in nums3 :
    sum2 += n
print(sum2)

print()
print("------------------------")
print()

# 예제 2: range 함수를 이용해 큰 수 연산하기

sum3 = 0
for n in range(1, 100) :
    sum3 += n
print(sum3)

print()
print()
print("------------------------")
print("--- 중첩 for문 구구단")
print("------------------------")
print()

'''
[f-string 문자열 포매팅 방식]

- 문자열 안에서 중괄호 {}안에 변수를 바로 넣거나, 계산식을 넣어서 결과를 문자열 안에 삽입해주는 역할
'''

#  예제 1. 2단부터 9단까지 출력하기
for x in range(2, 10) :
    for y in range(1, 10) :
        print(f"{x} X {y} = {x * y}")
    print()
print()

print("------------------------")
print("--- 리스트")
print("------------------------")
print()

'''
[컬렉션 자료형 - 리스트(list)]

- 일상 생활에서 사용하는 목록과 비슷한 개념을 가진 자료구조
- 여러 개의 데이터를 하나의 변수에 한 번에 저장하고 관리할 수 있다.
- 하나의 데이터만 담은 변수
    - age = 20
- 여러 개의 데이터를 묶은 리스트를 담은 변수
    - nums = [0, 1, 2, 3] 데이터들을 쉼표로 구분하여 나열한다.
'''

'''
numbers = [0, 1, 2, 3, 4]       # 숫자 리스트
alphabets = ['a', 'b', 'c']     # 문자 리스트
bools = [True, True, False]     # 논리값 리스트
greetings = ["hi", "hello"]     # 문자열 리스트

# 파이썬에서만 가능 (다른 언어에서는 사용 불가)
example = [3, 9, "y", 2, "k", True]     # 숫자, 문자, 논리값 혼합하여 담은 리스트

# 리스트 슬라이싱
리스트[start : stop : step]

# IndexError
nums = [1, 2, 3, 4, 5]      # 인덱스는 5까지 있다
print(nums[7])              # IndexError: list index out of range
'''

# 예제 1
nums = [6, 1, 3]
print(nums)

print()
print("------------------------")
print()

# 예제 2. 인덱스를 사용하여 요소 접근하기
names = ["kim", "lee", "park"]
print(names[0])
print(names[1])
print(names[2])
print(names[-1])
print(names[-2])
print(names[-3])

print()
print("------------------------")
print()

# 예제 3
nums = [10, 20, 30, 40, 50]
print(nums[0])
print(nums[2])
print(nums[4])
print(nums[2])

print()
print()
print("------------------------")
print("--- 리스트 슬라이싱")
print("------------------------")
print()

# 예제 1
example = [3, 9, "y", 2, "k", True]
print(example[1:4])
print(example[2:])
print(example[0:-1])

print()
print()
print("-----------------------------")
print("--- 리스트 결합 : + 연산자")
print("-----------------------------")
print()

'''
[리스트 결합]

- 리스트에서 자주 사용하는 연산 중 하나는 결합이다.
- 리스트 결합은 여러 개의 리스트를 하나의 리스트로 합쳐 새로운 리스트를 만들 수 있는 연산이다.

[+ 연산자]

- '+' 연산자 - 두개 이상의 리스트를 직접 연결하여 새로운 리스트를 만든다.
- 기존 리스트를 수정하지 않는다.
'''

# 예제 1
list1 = ["A", "B", "C"]
list2 = ["D", "E"]
list3 = list1 + list2
print(list3)
list3 = list2 + list1
print(list3)

print()
print()
print("---------------------------")
print("--- 리스트 결합 : extend")
print("---------------------------")
print()

'''
[extend()]

- 메서드 - 기존 리스트의 끝에 다른 리스트의 모든 요소를 추가한다.
- 기존 리스트를 수정한다.
- 메모리에 효율적이다
- 문법 : 리스트.extend(연결할 리스트)
'''

# 예제 1
list11 = ["A", "B", "C"]
list22 = ["D", "E"]
list11.extend(list22)
print(list11)
print(list22)

print()
print("------------------------")
print()

# 예제 2
nums1 = [1, 2, 3]
nums2 = [4, 5]
nums1.extend(nums2)
print(nums1)

print()
print()
print("------------------------")
print("--- 리스트 반복")
print("------------------------")
print()

nums1 = [1, 9, 3, 0]
print(nums1 * 3)

print()
print()
print("---------------------------")
print("--- 리스트 추가 : append")
print("---------------------------")
print()


'''
[리스트 메서드]

1. append()
    - 리스트에 요소를 추가하고 싶을 때 간단하게 쓰는 메서드.
    - 리스트의 마지막에 새로운 요소를 추가하는 역할.
    - 문법 : 리스트변수.append(추가할 값(요소))
'''

# 예제 1
nums4 = [1, 2, 3]
nums4.append(4)
print("추가 후 : ", nums4)

print()
print("------------------------")
print()

# 예제 2
fruits = ["apples", "bananas"]
fruits.append("cherry")
print("추가 후 : ", fruits)

print()
print()
print("---------------------------")
print("--- 리스트 추가 : insert")
print("---------------------------")
print()

'''
[리스트 메서드]

2. insert()
    - 파이썬에서는 리스트의 중간에 요소를 삽입할 수 있는 insert() 메서드를 제공
    - 문법 : 리스트변수.insert(위치(인덱스 번호), 추가할 값(요소))
'''

# 예제 1
nums5 = [4, 5, 6]
print("추가 전 : ", nums5)
nums5.insert(1, 8)
print("추가 후 : ", nums5)

print()
print()
print("-----------------------------------")
print("--- 리스트 추가 : append, insert")
print("-----------------------------------")
print()

# 예제
animals = ["monkey", "dog"]
print("추가 후 :", animals)
animals.append("cat")
animals.append("lion")
print("결과 1 :", animals)
animals.insert(2, "horse")
print("결과 2 :", animals)
animals.insert(4, "cow")
print("결과 3 :", animals)

print()
print()
print("----------------------------")
print("--- 리스트 삭제 : remove")
print("----------------------------")
print()

'''
[리스트 메서드]

3. remove()
    - 특정 값을 가진 요소를 삭제
    - 문법 : 리스트변수.remove(요소)
'''

# 예제 1
nums6 = [1, 2, 3, 4, 5]
print("추가 전 : ", nums6)
nums6.remove(2)
print("추가 후 : ", nums6)

print()
print("------------------------")
print()

# 예제 2: 여러 개의 요소가 있을 때 remove() 메서드 사용 예제
print(">> 리스트 삭제 예제 2: 여러 개의 요소가 있을 때 remove() 메서드 사용 예제")

color = ["black", "yellow", "red", "black"]

# remove는 왼쪽에서 오른쪽 방향으로 순차적으로 검사하여 처음 발견되는 값과 일치하는 요소만 삭제
# 동일한 값을 가진 요소가 여러 개 있더라도 처음 발견된 요소만 삭제한다.
color.remove("black")

# while문 사용하여 remove
while "black" in color :
    color.remove("black")
print(color)

# 오류 : x not in list 리스트에 없는 값
# color.remove("hello")
print(color)

print()
print()
print("------------------------")
print("--- 리스트 삭제 : pop")
print("------------------------")
print()

'''
[리스트 메서드]

4. pop()
    - 특정 위치에 있는 요소를 삭제
    - 문법 : 리스트변수.pop(인덱스 번호)
'''

# 예제 1
nums7 = [1, 2, 3, 4, 5]
print("추가 전 : ", nums7)
nums7.pop(4)
print("추가 후 : ", nums7)

print()
print("------------------------")
print()

# 예제 2
colors = ["black", "yellow", "red", "black"]
colors.pop(3)
print(colors)

print()
print("------------------------")
print()

# 예제 3
numbers = [10, 20, 30, 40, 50]
numbers.pop(2)
print(numbers)

print()
print()
print("------------------------")
print("--- 리스트 길이 확인")
print("------------------------")
print()

'''
[리스트 메서드]

5. len()
    - 리스트 길이
    - 문법 : len(리스트)
'''

# 예제 1
computer_science = ["data structure", "algorithms", "python"]
subject_num = len(computer_science)
print(subject_num)

print()
print()
print("------------------------ 끝")
print()

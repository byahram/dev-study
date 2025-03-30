"""
2025.03.21 금
"""

print("------------------------")
print()

# break문 예제 1
print(">> break문 예제 1")

count = 0
while count < 10 :
    print(count)
    count += 1
    if count == 5 :
        break
print()

# break문 예제 2
print(">> break문 예제 2")

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

# continue문 예제 1
print(">> continue문 예제 1")

num = 0
while num < 20 :
    num += 1
    if num % 3 == 0 :
        continue
    print(num, end=" ")     # end = " " 숫자 사이에 띄어쓰기 하나를 추가한다. 
                            # end = "," 숫자 사이에 쉼표를 추가
print("\n")

# continue문 예제 2
print(">> continue문 예제 2")

num2 = 0
while num2 < 20 :
    num2 += 1
    if num2 % 3 == 0 :
        print("짝", end = " ")
        continue
    print(num2, end=" ")
print("\n")

# break문과 continue문 예제 1
print(">> break문과 continue문 예제 1")

num3 = 0
while num3 < 20 :
    num3 += 1
    if num3 % 3 == 0 :
        continue
    if num3 == 17 :
        break
    print(num3, end = " ")
print("\n")

# 구구단 예제 1
print(">> 구구단 예제 1")

dan = 2
while dan <= 9 :
    n = 1
    while n <= 9 :
        print("{}x{}={}".format(dan, n, dan * n))
        n += 1
    print()
    dan += 1
print("\n")

# 중첩 while문을 사용하여 별찍기 예제 1
print(">> 중첩 while문을 사용하여 별찍기 예제 1")

row = 1
while row < 6 :
    star = 1
    while star <= row :
        print("*", end="")
        star += 1
    print()
    row += 1
print()

print("------------------------")
print()

# for문 예제 1
print(">> for문 예제 1")

for n in [1, 2, 3, 4, 5] :
    print(n)
print()

# for문 예제 2
print(">> for문 예제 2")

names = ["jennie", "hani", "kelly"]
for name in names :
    print(name)
print()

# for문 예제 3
print(">> for문 예제 3")

for ch in "Hello" :
    print(ch)
print()

for str in "nice" :
    print(str)
print()

# for문을 활용한 합 구하기 예제
print(">> for문을 활용한 합 구하기 예제")

nums = [1, 2, 3, 4, 5]
sum = 0
for n in nums :
    sum += n
print(sum)
print()

# 리스트 안의 숫자들을 모두 곱해 결과 구하는 예제
print(">> 리스트 안의 숫자들을 모두 곱해 결과 구하는 예제")

nums2 = [1, 2, 3, 4, 5]
result = 1
for n in nums2 :
    result *= n
print(result)
print()

print("------------------------")
print()

# range 예제 1
print(">> range 예제 1")

nums3 = range(1, 6)
sum2 = 0
for n in nums3 :
    sum2 += n
print(sum2)
print()

# range 예제 2: range 함수를 이용해 큰 수 연산하기
print(">> range 예제 2: range 함수를 이용해 큰 수 연산하기")

sum3 = 0
for n in range(1, 100) :
    sum3 += n
print(sum3)
print()

print("------------------------")
print()

# 중첩 for문 예제 1
print(">> 중첩 for문 예제 1: 2단부터 9단까지 출력하기")

for x in range(2, 10) :
    for y in range(1, 10) :
        print(f"{x} X {y} = {x * y}")
    print()
print()

print("------------------------")
print()

# 리스트 예제 1
print(">> 리스트 예제 1")

nums = [6, 1, 3]
print(nums)

# 인덱스를 사용하여 요소 접근하기
names = ["kim", "lee", "park"]
print(names[0])
print(names[1])
print(names[2])
print(names[-1])
print(names[-2])
print(names[-3])
print()

# 리스트 예제 2
print(">> 리스트 예제 2")

nums = [10, 20, 30, 40, 50]
print(nums[0])
print(nums[2])
print(nums[4])
print(nums[2])
print()

print("------------------------")
print()

# 리스트 슬라이싱 예제 2
print(">> 리스트 슬라이싱 예제 2")

example = [3, 9, "y", 2, "k", True]
print(example[1:4])
print(example[2:])
print(example[0:-1])
print()

print("------------------------")
print()

# 리스트 결합 : + 연산자
print(">> 리스트 결합 : + 연산자")

list1 = ["A", "B", "C"]
list2 = ["D", "E"]
list3 = list1 + list2
print(list3)
list3 = list2 + list1
print(list3)
print()

# 리스트 결합 : extend
print(">> 리스트 결합 : extend")

list11 = ["A", "B", "C"]
list22 = ["D", "E"]
list11.extend(list22)
print(list11)
print(list22)
print()

# 리스트 결합 : extend
print(">> 리스트 결합 : extend")

nums1 = [1, 2, 3]
nums2 = [4, 5]
nums1.extend(nums2)
print(nums1)
print()

# 리스트 반복 예제
print(">> 리스트 반복 예제")

nums1 = [1, 9, 3, 0]
print(nums1 * 3)
print()

print("------------------------")
print()

# 리스트 추가 append 예제 1
print(">> 리스트 추가 append 예제 1")

nums4 = [1, 2, 3]
nums4.append(4)
print("추가 후 : ", nums4)
print()

# 리스트 추가 append 예제 2
print(">> 리스트 추가 append 예제 2")

fruits = ["apples", "bananas"]
fruits.append("cherry")
print("추가 후 : ", fruits)
print()

print("------------------------")
print()

# 리스트 추가 insert 예제 1
print(">> 리스트 추가 insert 예제 1")

nums5 = [4, 5, 6]
print("추가 전 : ", nums5)
nums5.insert(1, 8)
print("추가 후 : ", nums5)
print()

# 리스트 추가 append, insert 예제
print(">> 리스트 추가 append, insert 예제")

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

print("------------------------")
print()

# 리스트 삭제 예제 1 : remove
print(">> 리스트 삭제 예제 1 : remove")

nums6 = [1, 2, 3, 4, 5]
print("추가 전 : ", nums6)
nums6.remove(2)
print("추가 후 : ", nums6)
print()

# 리스트 삭제 예제 2: 여러 개의 요소가 있을 때 remove() 메서드 사용 예제
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

# 리스트 삭제 예제 3 : pop
print(">> 리스트 삭제 예제 3 : pop")

nums7 = [1, 2, 3, 4, 5]
print("추가 전 : ", nums7)
nums7.pop(4)
print("추가 후 : ", nums7)
print()

# 리스트 삭제 예제 4 : pop
print(">> 리스트 삭제 예제 4 : pop")

colors = ["black", "yellow", "red", "black"]
colors.pop(3)
print(colors)
print()

# 리스트 삭제 예제 5 : pop
print(">> 리스트 삭제 예제 5 : pop")

numbers = [10, 20, 30, 40, 50]
numbers.pop(2)
print(numbers)
print()

print("------------------------")
print()

# 리스트 길이 확인 예제 1
print(">> 리스트 길이 확인 예제 1")

computer_science = ["data structure", "algorithms", "python"]
subject_num = len(computer_science)
print(subject_num)
print()

print("------------------------")
print()

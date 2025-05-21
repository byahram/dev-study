# 41. 리스트 조건 추출하기
print("[41.]")
animals = ["dog", "cat", "rabbit", "cow", "goat", "sheep", "mouse"]
animal3 = []
for i in animals :
    if len(i) == 3 :
        animal3.append(i)
print(animal3)
print()

# 42. 리스트를 활용한 반복문 할당
print("[42.]")
dot = [1.5, 3.6, 4.53, 5.48, 6.87, 7.87, 8.89]
dot100 = []

for i in dot :
    dot100.append(i * 100)
print(dot100)

a = 0
while a < len(dot):
    dot100[a] = dot[a] * 100
    a += 1
print(dot100)
print()

# 43. 리스트 요소의 평균 구하기
print("[43.]")
score = [60, 75, 85, 85, 85, 90, 70, 90, 80]
avg = sum(score) / len(score)

# 2.
# total = 0
# for i in score :
#     total += i
# avg = total / len(score)
print(avg)
print()

# 44. 해론의 공식 구현하기
print("[44.]")
a, b, c = 5, 6, 7
s = (a + b + c) / 2
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
print("삼각형의 넓이는 %f입니다." % area)
print()

# 45. 문자열 슬라이싱 1
print("[45.]")
num_list = [100, 101, 102, 103, 104, 105, 106, 107, 108]
odd = []
for i in num_list :
    if i % 2 == 1 :
        odd.append(i)
print(odd)
print(num_list[1::2])
print()

# 46. 문자열 슬라이싱 2
print("[46.]")
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(num_list[2::3])
print()

# 47.
print("[47.]")
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(nums[::-1])
print()

# 48. split() 리스트화
print("[48.]")
message = "나는/너를/사랑해"
print(message.split("/"))
print()

# 49. 리스트와 리스트 합치기
print("[49.]")
A_student = ["김민수", "이민수", "박민수", "황민수", "곽민수", "권민수"]
B_student = ["김은혜", "이은혜", "박은혜", "황은혜", "곽은혜", "권은혜"]
A_student.extend(B_student)
print(A_student)
print()

# 50. count(), len() 리스트 갯수 연산하기
print("[50.]")
results = [True, False, False, True, False, True, True, False, True]
print("리스트 results는 총 {}개의 요소를 가지고 있고, True는 {}개 False는 {}개입니다.".format(len(results), results.count(True), results.count(False)))
print()

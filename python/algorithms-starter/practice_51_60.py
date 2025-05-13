# 51. 튜플 할당하기
print("[51.]")
noodle = (700, "왕라면", 65.8, True)
print(noodle)
print(type(noodle))
print()

# 52. 수정이 불가능한 튜플의 특징 
print("[52.]")
nums = (1, 2, 3, 3, 4, 5)
# nums.append(6)
# print(nums)       # AttributeError: 'tuple' object has no attribute 'append'
print()

# 53. 튜플에서 사용가능한 함수
print("[53.]")
nums = (1, 2, 3, 3, 4, 5)
print("튜플의 총 길이는 {}이고 최댓값은 {}, 최솟값은 {}입니다.".format(len(nums), max(nums), min(nums)))
print()

# 54. 문자열의 튜플 형변환
print("[54.]")
text = "가나라다마바사"
print(tuple(text))
print()

# 55. 튜플 데이터 이용하기
print("[55.]")
nums = (1, 2, 3, 4, 5)
list_nums = list(nums)

for i in range(6, 31) :
    list_nums.append(i)
    i += 1

# i = 6
# while i <= 30 :
#     list_nums.append(i)
#     i += 1

print(nums)
print(list_nums)
print()

# 56. 튜플의 장점, 데이터 용량 출력하기
print("[56.]")
import sys
tnums = (1, 2, 3, 4, 5)
lnums = [1, 2, 3, 4, 5]
print("튜플 tnums과 리스트 lnums의 메모리 사이즈는 각각 {} bytes, {}bytes 입니다.".format(sys.getsizeof(tnums), sys.getsizeof(lnums)))
print()

# 57. 튜플 슬라이싱
print("[57.]")
# rainbow = ("빨", "주", "노", "초", "파", "남", "보")
rainbow = "빨", "주", "노", "초", "파", "남", "보"
print(rainbow[:4])
print(rainbow[2::2])
print(rainbow[-1:-4:-1])
print()

# 58. range 함수를 이용한 튜플 선언 
print("[58.]")
nums = tuple(range(100, 80, -2))
print(nums)
print()

# 59. range 함수를 이용한 튜플 값 합계 구하기 
print("[59.]")
nums = tuple(range(1, 1501))
print(sum(nums))

total = 0
for i in nums :
    total += i
print(total)
print()

# 60. 집합 기본형 알아보기 
print("[60.]")
a = 7
b = 3.14
c = True
d = (1, 2, 3)
e = [1, 2]
set1 = a, b, c, d, e
print(set1)
print()

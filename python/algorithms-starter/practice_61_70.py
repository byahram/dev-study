# 61. 집합 항목 추가하기
print("[61.]")
set1 = {1, 2, 3, 4, 5}
list1 = [11, 12, 13, 14, 15]

for i in range(6, 11) :
    set1.add(i)

set1.update(list1)
print(set1)
print()

# 62. 합집합 구하기
print("[62.]")
odd_nums = {1, 3, 5, 7, 9}
even_nums = {2, 4, 6, 8, 10}
nums = odd_nums.union(even_nums)
print("집합 set1은 {}, 집합 set2는 {}이고 \n두 집합의 합집합 set3는 {}입니다.".format(odd_nums, even_nums, nums))
print()

# 63. 집합 요소 제거하기
print("[63.]")
nums = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

for i in range(1, 10, 2) :
    nums.remove(i)

print(nums)
print()

# 64. 리스트 컴프리핸션 및 교집합 구하기
print("[64.]")
multiple2 = [i for i in range(2, 100, 2)]
multiple3 = [i for i in range(3, 100, 3)]
print(set(multiple2) & set(multiple3))
print(set(multiple2).intersection(set(multiple3)))
print()

# 65. 딕셔너리 선언하기
print("[65.]")
monitor = {
    "C27R502" : 219000,
    "24MP400" : 181450,
    "C27G54T" : 336890,
    "Q32V3S" : 337640,
}
print(monitor)
print()

# 66. 딕셔너리 데이터 추가하기
print("[66.]")
new_mo = {
    "32QN650" : 398610, 
    "24MK430H" : 185600
}
monitor.update(new_mo)

# monitor["32QN650"] = 398610
# monitor["24MK430H"] = 185600
print(monitor)
print()

# 67. 딕셔너리 keys()와 values() 사용하기
print("[67.]")
monitor_key = monitor.keys()
monitor_value = monitor.values()
print(list(monitor_key))
print(list(monitor_value))
print()

# 68. keyㅌㅌ 값 반복 출력하기
print("[68.]")
animals = {
    "개" : "dog",
    "고양이" : "cat",
    "소" : "cow", 
    "양" : "sheep"
}

for i in animals :
    print(i, end=" ")
print('\n')

# 69. value 값 반복 출력하기
print("[69.]")
animals = {
    "개" : "dog",
    "고양이" : "cat",
    "소" : "cow", 
    "양" : "sheep"
}

for i in animals.values() :
    print(i, end=" ")
print('\n')

# 70. items() 사용, 반복 출력하기
print("[70.]")
animals = {
    "개" : "dog",
    "고양이" : "cat",
    "소" : "cow", 
    "양" : "sheep"
}

for key, value in animals.items() :
    print(f"key = {key}, value = {value}")
print()

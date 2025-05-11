# 31. replace()
print("[31.]")
population = "51,820,000"
population = int(population.replace(",", ""))
print(type(population))
print(population)
print()

# 32. split()
print("[32.]")
data = "1948-08-15"
print(data.split("-"))
print()

# 33. 리스트 인덱스 사용 및 문자열 포매팅
print("[33.]")
member = ["홍길동", 185.4, 86]
print(f"{member[0]} 회원님의 키는 {member[1]}이고 몸무게는 {member[2]}입니다.")
print()

# 34. 리스트 선언 및 출력
print("[34.]")
menu = ["햄버거", "피자", "치킨", "부닭찌개", "족발"]
print(menu)
print()

# 35. 리스트 선언 및 출력
print("[35.]")
food_list = ["햄버거", "피자", "치킨", "부닭찌개", "족발"]
food_list.append("김밥")
print(food_list)
print()

# 36. 리스트 요소 삭제하기
print("[36.]")
food_list = ["햄버거", "피자", "치킨", "부닭찌개", "족발", "김밥"]
food_list.pop(1)
food_list.pop(1)
# del food_list[1:3]
print(food_list)
print()

# 37. 리스트 요소 교체하기
print("[37.]")
food_list = ["햄버거", "피자", "치킨", "부닭찌개", "족발", "김밥"]
food_list[3] = "부대찌개"
print(food_list)
print()

# 38. 리스트 요소 삭제하기
print("[38.]")
AmongUs = ["시민", "시민", "임포스터", "시민", "시민", "시민", "시민"]
AmongUs.remove("임포스터")
print(AmongUs)
print()

# 39. 리스트 값 삽입하기 - insert()
print("[39.]")
food_list = ["햄버거", "피자", "치킨", "부닭찌개", "족발", "김밥"]
food_list.insert(4, "불고기")
print(food_list)
print()

# 40. 리스트 최대값, 최소값 구하기
print("[40.]")
num_list = [1, 3, 5, 7, 11, 123, 1240, 9999]
print(f"최솟값은 {min(num_list)}이고 최댓값은 {max(num_list)}입니다.")
print()

'''
2025.05.08 목
'''

print()
print()
print("------------------------")
print("--- 이진 탐색")
print("------------------------")
print()

'''
[이진 트리 정의] 

- 각 노드가 최대 두 개의 자식 노드를 갖는 계층적 자료 구조이다.

[이진 탐색]

- 정렬된 배열이나 리스트에서 중간값을 기준으로, 반씩 탐색 범위를 줄여나가며 원하는 값을 빠르게 찾는 알고리즘이다.

    arr = [1, 3, 5, 7, 9, 11]
    target = 7

    가운데 값 : 5 -> 탐색[7, 9, 11]
    다시 가운데 값 : 9 -> 7
'''

# 이진탐색
def binary_search(arr, target) :
    left = 0                # 탐색할 범위의 시작 인덱스
    right = len(arr) - 1    # 탐색할 범위의 끝 인덱스

    # left가 right보다 작거나 같을 때까지 반복 (탐색 구간이 남아있는 동안)
    while left <= right :
        # 중간 인덱스를 계산
        mid = (left + right) // 2        # 나는 몫만 가져온다는 뜻이다.

        # 중간 값이 찾고자 하는 값과 같으면 인덱스 반환
        if arr[mid] == target :
            return mid

        # 중간 값이 더 작으면 오른쪽 구간에서 계속 탐색
        elif arr[mid] < target :
            left = mid + 1      # 현재 중간값 arr[mid]가 우리가 찾는 값 target보다 작음
                                # 그러면 찾는 값은 오른쪽에 있을 수 밖에 없음
                                # 그래서 왼쪽 구간을 버리고, left를 오른쪽으로 옮겨서 탐색 범위를 좁힘
                                # arr = [2, 4, 6, 8, 10]
                                # target = 9
                                # mid = 2       arr[2] = 6
                                # 6 < 9 -> 오른쪽 절반 탐색
                                # -1

        else :
            right = mid - 1

    # 끝까지 못찾으면 -1 반환
    return -1

# 오름차순으로 정렬된 리스트
arr = [2, 4, 6, 8, 10, 12, 14]

# 찾고자 하는 값
target = 10

# 이진탐색 함수 호출
result = binary_search(arr, target)

# 결과 출력
if result != -1 :
    print(f"{target}은 {result}에 있습니다.")
else :
    print(f"{target}은 리스트에 없습니다.")
    
print()
print()
print("------------------------ 끝")
print()

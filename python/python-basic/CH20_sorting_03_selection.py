'''
2025.05.08 목
'''

print()
print()
print("--------------------------")
print("--- 자료구조 - 선택 정렬")
print("--------------------------")
print()

'''
[자료구조 - 선택 정렬]

- 리스트에서 가장 작은 값을 찾아서 맨 앞 값과 바꾼다.
- [5, 3, 8, 4, 2] -> [2, 3, 8, 4, 5]
- 그 다음에는 두 번째 작은 값을 두 번째 자리에... 총 n-1번 반복된다

[선택 정렬 동작 방식]

1. 왼쪽부터 차례로 하나씩 선택함
2. 오른쪽에 있는 값들 [j] 전부 검사
3. 찾은 값과 현재 위치의 값 교환
4. 다음 위치로 넘어가서 반복
'''

# 선택 정렬
def selection_sort(arr) :
    n = len(arr)

    for i in range(n) :         # i는 정렬되지 않은 구간의 시작 인덱스
        min_idx = i         # 현재 위치를 최소값이라고 가정
        for j in range(i+1, n) :        # 나머지 원소들과 비교하여
            if arr[j] < arr[min_idx] :          # 더 작은 값을 찾으면
                min_idx = j

        # i번째 위치와 최소값의 위치 교환
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

print("선택 정렬 결과 :", selection_sort([5, 3, 8, 4, 2]))

'''
[선택 정렬]

[5, 3, 8, 4, 2]

1회전 i = 0    
min_idex = i = 0    # arr[0] = 5

    j = 1 to 4

    j = 1
    if arr[1] < arr[min_idx]
    if 3 < 5    # 참
        min_idx = 1   arr[1] = 3

    j = 2 
    if arr[2] < arr[min_idx] 
    if 8 < 3    # 거짓

    j = 3
    if  arr[3] < arr[min_dex]
    if 4 < 3    # 거짓

    j = 4
    if  arr[4]  < arr[min_idx]
    if 2 < 3    # 참
        min _idx = 4

    arr[0], arr[4] = arr[4], arr[0]
    1회전 결과 : [2, 3, 8, 4, 5]

2회전  i = 1    [2, 3, 8, 4, 5]
3회전  i = 2    [2, 3, 4, 8, 5]
4회전  i = 3    [2,3,4,5,8]
5회전  i = 4    # 비교 없음
'''

print()
print()
print("------------------------ 끝")
print()

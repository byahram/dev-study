"""
2025.04.29 화
"""

print()
print()
print("------------------------")
print("--- 큐(Queue)란?")
print("------------------------")
print()

'''
[큐(Queue)]

- 데이터를 순서대로 저장하고 꺼내는 선형자료구조로 먼저 들어간 데이터가 먼저 나오는 선입선출(FIFO, First In First Out) 구조이다.
- [Front] => 1 -> 2 -> 3 
    : 1이 가장 먼저 들어와서 가장 먼저 나간다.

[실생활 예시]

- 버스 정류장 줄서기 : 먼저 선 사람부터 탑승
- 프린터 작업 대기열 : 먼저 보낸 문서부터 출력
- https://velog.io/@sbinha/%EC%8A%A4%ED%83%9D-%ED%81%90

[왜 큐가 필요할까?]

1. 순차적인 작업 처리가 필요한 곳에 적합
2. 실시간 처리 시스템(프린터, 요청 처리등에 사용)
3. BFS(너비 우선 탐색)와 같은 알고리즘에서 핵심 자료구조로 활용

[핵심 개념(필요한 함수)]

- Enqueue(인큐) : 데이터를 뒤쪽에서 넣는 작업
- Dequeue(디큐) : 데이터를 앞쪽에서 꺼내는 작업
- Peek : 삭제 없이 가장 앞의 데이터를 확인
- isEmpty : 큐가 비어있는지 확인
'''

# 리스트로 큐 구현 (비효율)
#   : 리스트는 배열처럼 생겨서, 앞에서 꺼내면 뒤에 있는 것을 전부 앞으로 밀어야 한다.
queue = []

# enqueue
queue.append("고객1")
queue.append("고객2")
queue.append("고객3")
print("현재 큐 :", queue)
print()

# dequeue : 값을 꺼내는 작업
print("처리 중 :", queue.pop(0))
print("처리 중 :", queue.pop(0))

print()
print("------------------------")
print()

# 효율적인 큐 구현

# deque 모듈 가져오기(큐 기능 사용하기 위해서)
from collections import deque

# 비어있는 큐 생성
queue = deque()

# 큐에 넣기 (enqueue)
queue.append("사과")
queue.append("바나나")
queue.append("체리")
print("현재 큐 :", queue)

print()
print()
print("------------------------ 끝")
print()
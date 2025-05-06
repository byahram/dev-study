"""
2025.05.02 금
"""

print()
print()
print("------------------------")
print("--- 큐(Queue)")
print("------------------------")
print()

'''
[큐(Queue)]

- 선입선출 : 데이터를 순서대로 저장하고 꺼내는 선형 자료구조
'''

# 큐 예제 1. 프린터 출력 대기열 시뮬레이션
from collections import deque

# 프린터 큐를 나타내는 클래스 정의
class PrinterQueue :
    # 생성자
    def __init__(self) :
        # 출력할 작업들을 저장할 큐
        self.jobs = deque()

    # 작업을 큐에 추가하는 메서드
    def add_job(self, job) :
        self.jobs.append(job)       # 큐의 뒤쪽에 작업 추가
        print(f"프린터 작업 추가 : {job}")

    # 작업을 큐에서 꺼내어 처리하는 메서드
    def process_job(self) :
        # 대기 중인 작업이 있으면
        if self.jobs :
            job = self.jobs.popleft()       # 큐의 앞쪽 작업 꺼냄
            # .pop : 오른쪽(뒤쪽) 요소를 꺼냄 -> 스택처럼 동작
            # .popleft : 왼쪽(앞쪽) 요소를 꺼냄 -> 큐처럼 동작

            print(f"프린터 출력 중 : {job}")

        # 대기 중인 작업이 없으면 (대기열이 비었을 경우)
        else :
            print("대기 중인 작업이 없습니다.")

# printerQueue 클래스의 인스턴스를 생성
printer = PrinterQueue()

# 출력할 작업 2개를 추가
printer.add_job("파일1.pdf")
printer.add_job("파일2.pdf")

# 작업을 하나씩 처리
printer.process_job()
printer.process_job()

print()
print("------------------------")
print()

# 큐 예제 2. 놀이공원 대기열 시뮬레이션

# 큐 선언
from collections import deque

# 놀이공원 입장 대기열을 관리하는 클래스
class partQueue :
    # 생성 
    def __init__(self) :
        self.line = deque()

    # 사람들이 줄을 서는 메서드(추가)
    def join_line(self, name) :
        self.line.append(name)
        print(f"{name}님이 줄을 섰습니다.")

    # 입장 처리 메서드(빼기)
    def enter_park(self) :
        if self.line :
            name = self.line.popleft()
            print(f"{name}님이 입장하셨습니다.")

        else :
            print("줄에 아무도 없습니다.")

queue = partQueue()

queue.join_line("철수")
queue.join_line("영희")
queue.join_line("길동")

queue.enter_park()
queue.enter_park()
queue.enter_park()

print()
print("------------------------ 끝")
print()

import sys
input = sys.stdin.readline

N,M = map(int, input().split())
answer = []
#yeah = "yeah"

def dfs(start):
    if len(answer) == M: #M길이랑 같으면 답출력
        print(*answer) #언패킹
        return

    for i in range(start, N+1): #1,2
        answer.append(i) #수더해줌
        dfs(i) #옆에 숫자 계산용
        answer.pop() #answer 초기화

dfs(1)



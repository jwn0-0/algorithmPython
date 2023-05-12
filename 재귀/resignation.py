import sys
input = sys.stdin.readline
T = []
P = []
N = int(input())
for i in range(N):
    t,p = map(int, input().split())
    T.append(t)
    P.append(p)
dp = [0 for _ in range(N+1)] # dp[i]는 i번째날까지 일을 했을 때, 최대값이다.

for i in range(N-1, -1, -1): #N이 7이면 i = 6,5,4,3,2,1,0
    if T[i] + i > N: # 상담에 필요한 일수가 퇴사일을 넘어가면
        #print(dp[i+1])
        dp[i] = dp[i+1] #다음날 값 그대로 가져옴
    else:
        #dp[i + 1] = 오늘 상담X, dp[T[i] + i] + P[i] = 오늘 상담  중 큰 값을 선택
        dp[i] = max(dp[i + 1], dp[T[i] + i] + P[i])

print(dp[0])

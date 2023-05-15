#14889
import sys
input = sys.stdin.readline
S =[]
N = int(input())
for _ in range(N):
    S.append(list(map(int, input().split())))
visited = [False for _ in range(N)] #n=4라면 visited = [1, 2, 3, 4] 선수
minvalue = sys.maxsize
def backtrack(depth, index):
    global minvalue
    #comination이 N/2일때
    if depth == N/2:
        #print(visited)
        startteam = linkteam = 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]: #startteam 선수 판별
                    startteam += S[i][j]
                elif not visited[i] and not visited[j]: #linkteam 선수 판별
                    linkteam += S[i][j]
        minvalue = min(minvalue, abs(startteam-linkteam))

    for i in range(index, N):
        if not visited[i]: #선정이 안되었더라면
            visited[i] = True
            backtrack(depth+1, i+1) #depth가 충족되어지고 돌아옴
            visited[i] = False #선택했던 선수를 false로 초기화


backtrack(0,0)
print(minvalue)


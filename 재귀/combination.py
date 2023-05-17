#10972
import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
for i in range(n - 1, 0, -1):
    if a[i - 1] < a[i]:
        target = i - 1
        break
    else:
        print(-1)
        sys.exit()

for i in range(n - 1, 0, -1):
    if a[target] < a[i]:
        a[target], a[i] = a[i], a[target]
        a = a[:target + 1] + sorted(a[target + 1:])
        print(*a)
        break




#N의 범위를 보았을때 백트래킹으로 풀면 안됨
"""
visited = [False]*(N+1)
combilist = []
combi =[]
def track():
    if len(combi) == N:
        combilist.append(list(combi))
        return

    for i in range(1,N+1):
        if not visited[i]:
            visited[i] = True
            combi.append(i)
            track()
            visited[i] = False
            combi.pop()

track()
for i in range(len(combilist)):
    if cinput == combilist[i]:
        if combilist[i] == combilist[-1]:
            print("-1")
        else:
            print(" ".join(map(str,combilist[i+1])))
"""

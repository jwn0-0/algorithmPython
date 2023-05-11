#18290
import sys
input = sys.stdin.readline
N,M,K = map(int, input().split())
num = []
existed = [[0]*(M+2)for _ in range(N+2)]
answer = 0
for i in range(N):
    num.append(list(map(int, input().split())))


def findmax():
    maxval = -40001
    for i in range(N):
        for j in range(M):
            if existed[i+1][j+1] == 0:
                maxval = max(maxval, num[i][j])
            else:
                continue
    return maxval

def changeexisted(i,j):
    r= i+1
    c= j+1
    existed[r][c]= 1
    existed[r-1][c] = 1
    existed[r+1][c] = 1
    existed[r][c-1] = 1
    existed[r][c+1] = 1

def checkifmax(maxval):
    for i in range(N):
        for j in range(M):
            if existed[i + 1][j + 1] == 0:
                if(num[i][j]==maxval):
                    #print(i,j,maxval)
                    changeexisted(i,j)
                    return 1
    return 0

for _ in range(K):
    maxval = findmax()
    if checkifmax(maxval):
        #print(answer, maxval)
        answer += maxval

print(answer)
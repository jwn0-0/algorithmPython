#6064
import sys
input = sys.stdin.readline

#시간초과
def answer(M, N, x, y):
    count = 0  # 몇 번째 해인지
    MM = NN = 0
    while True:
        if MM == M:
            MM = 0
        elif NN == N:
            NN = 0
        count += 1
        MM += 1
        NN += 1
        if (MM == x and NN == y): #x,y가 일치했을때
            break
        elif (MM == M and NN == N): #끝까지 갔지만 유효하는게 없을때
            count = -1
            break
    return count

def anotherway(M, N, x, y):
    k = x
    while k<=M*N:
        if((k-y)%N == 0):
            return k
        k += M
    return -1

T = int(input())
#2차원 배열 저장하기
num = [list(map(int, input().split())) for _ in range(T)]
for i in range(T):
    #print(answer(num[i][0], num[i][1], num[i][2], num[i][3]))
    print(anotherway(num[i][0], num[i][1], num[i][2], num[i][3]))


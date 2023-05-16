#2529
import sys
input = sys.stdin.readline
#입력
k = int(input())
equality = (list(input().split()))
visited = [False]*10
answer = []
combination = []
def checknum(index, num):
    if equality[index] == '<':
        return answer[index] < num
    else:
        return answer[index] > num
#숫자는 0부터 9까지 , 처음 index0부터
def backtracking(numlength):
    if numlength == k+1:
        combination.append(list(answer))
        return

    for i in range(10):
        if not visited[i]:
            if numlength == 0 or checknum(numlength-1,i):
                visited[i] = True
                answer.append(i)
                #print(str(i)+" appended, answer list = " + str(answer))
                backtracking(numlength+1)
                visited[i] = False
                answer.pop()

backtracking(0)
#최대값
print(''.join(map(str,combination[-1])))
#최소값
print(''.join(map(str,combination[0])))


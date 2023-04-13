
N = int(input())
candy = []
maxCount = 0

for i in range(N):
    candy.append(list(map(str, input())))

def checkwidth():
    global maxCount
    for i in range(N):
        count = 1
        for j in range(N-1):
            if(candy[i][j] == candy[i][j+1]):
                count+=1
                #증가시킨 값과 최대 사탕개수를 비교
                maxCount = max(count, maxCount)
            else:
                count = 1

def checkheight():
    for j in range(N):
        global maxCount
        count = 1
        for i in range(N-1):
            if (candy[i][j] == candy[i+1][j]):
                count += 1
                # 증가시킨 값과 최대 사탕개수를 비교
                maxCount = max(count, maxCount)
            else:
                count = 1

for i in range(N):
    for j in range(N-1):
        if(candy[i][j] != candy[i][j+1]):
            candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]
            checkwidth()
            checkheight()
            candy[i][j + 1], candy[i][j] = candy[i][j], candy[i][j+1]
        if(candy[j][i] != candy[j+1][i]):
            candy[j][i], candy[j+1][i] = candy[j+1][i], candy[j][i]
            checkwidth()
            checkheight()
            candy[j + 1][i], candy[j][i] = candy[j][i], candy[j+1][i]

print(maxCount)
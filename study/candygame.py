
N = int(input())
candy = []
maxCount = 0

#값 읽기
for i in range(N):
    candy.append(list(map(str, input())))

#열을 오른쪽으로 이동하면서 같은게 있음 카운트 증가(최종 맥스카운트에 반영)
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
#행을 아래로 이동하면서 같은게 있음 카운트 증가(최종 맥스카운트에 반영)
def checkheight():
    global maxCount
    for j in range(N):
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
        #같은 열에서 2개 색이 다를경우 바꿔보고 체크한담에 원래대로 돌려놈
        if(candy[i][j] != candy[i][j+1]):
            candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]
            checkwidth()
            checkheight()
            candy[i][j + 1], candy[i][j] = candy[i][j], candy[i][j+1]
        #같은 행에서 2개 색이 다를경우 바꿔보고 체크한담에 원래대로 돌려놈
        if(candy[j][i] != candy[j+1][i]):
            candy[j][i], candy[j+1][i] = candy[j+1][i], candy[j][i]
            checkwidth()
            checkheight()
            candy[j + 1][i], candy[j][i] = candy[j][i], candy[j+1][i]

print(maxCount)
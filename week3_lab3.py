from bisect import bisect_left


num = int(input())
columns = list(map(int, input().split()))
answer = []

for i in range(num):

    if i == 0:
        answer.append(columns[i])
        continue

    if answer[-1] < columns[i]:
        answer.append(columns[i])
    else:
        answer[bisect_left(answer, columns[i])] = columns[i]

print(num-len(answer))
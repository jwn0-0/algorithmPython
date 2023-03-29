import sys
T=int(input())
book1_num = int(input())
book1 = list(map(int, sys.stdin.readline().split()))
book2_num = int(input())
book2 = list(map(int, sys.stdin.readline().split()))
def findnum(target):
    start = min(book1)
    end = max(book1)
    correct = 0
    while start <= end:
        mid = start + end //2
        if(target == mid or target == end):
            correct = 1
            break
        elif(target < mid):
            end = mid -1
        elif(target > mid):
            start = mid + 1
    return correct

for i in range(book2_num):
    print(findnum((book2[i])))

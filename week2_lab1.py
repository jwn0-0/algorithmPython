import sys
#배열처리 할때는   sys 사용시에 시간을 줄일 수 있음
K, N = map(int, input().split())
lan = [int(sys.stdin.readline()) for _ in range(K)]  # 11
start, end = 1, max(lan)  # 이분탐색 처음과 끝위치
while start <= end:  # 적절한 선의 길이를 찾는 알고리즘
    mid = (start + end) // 2  # 중간 위치
    print('mid:', mid, end=" ")
    lines = 0  # 선 수
    for i in lan:
        lines += i // mid  # 분할 된 선 수
        print('lines:', lines)

    if lines >= N:  # 선의 개수가 분기점
        start = mid + 1
    else:
        end = mid - 1
print('end:', end)
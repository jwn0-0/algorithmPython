import sys

input = sys.stdin.readline
N, A = map(int, input().split())  # N개 값 , A일
dt = list(map(int, input().split()))

if max(dt) == 0:
    print('none')
else:
    # value initialize
    value = sum(dt[:A])  # A개로 나누어 sum을 구함
    max_V = value
    max_C = 1

    for i in range(A, N):  # A ~ N-1
        # 슬라이딩 윈도우
        value = value + dt[i]  # 윈도앞 값
        value = value - dt[i - 1]  # 윈도 뒤의 값

        # 최대값을 찾음

        if value > max_V:
            max_V = value


        # 최대값의 횟수 count
        elif value == max_V:
            max_C += 1
    print(max_V)
    print(max_C)
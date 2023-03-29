import sys
N = int(input())
a = list(map(int, sys.stdin.readline().split()))
count = 0
for i in range(N-1):
    if(a[i+1]<a[i]):
        count += 1

print(count)
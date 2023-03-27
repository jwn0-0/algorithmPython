N = int(input())
A= list(map(int,input().split()))
B= list(map(int,input().split()))

A.sort()
total = 0
for i in range(N):
    total += A[i] * max(B)
    B.remove(max(B))

print(total)
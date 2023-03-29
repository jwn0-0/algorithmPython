N = int(input())
count = 0
#split을 사용하지않음
a = list(map(int, input()))
for i in range(N):
    count += a[i]
print(count)
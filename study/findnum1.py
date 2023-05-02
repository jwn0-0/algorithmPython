#1748
import sys
import math
input = sys.stdin.readline

N = input() #len을 활용하기 위해서 int사용 x
numlength = len(N) - 1 #자리수
n = int(N)

count = 0
#자리수 이전까지의 합
for i in range(1,numlength):
    count += (int(math.pow(10,i)) - int(math.pow(10,i-1) )) * i
#120이면 100~120까지
calculate = int(math.pow(10,numlength-1))
count += ((n - calculate) + 1 ) * numlength
print(count)


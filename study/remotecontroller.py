#1107
import sys
input = sys.stdin.readline()
target = int(input())
M = int(input())
broken = list(map(int, input().split()))
print(broken)
#+, - 만 사용하여 이동 abs = 절댓값
min_count = abs(100 - target)


for k in range(1000001):
    nums = str(k)
    for j in range(len(nums)):
        #각 숫자가 고장났는지 확인, 고장이면 break 0~999999까지 가면서 리모컨 버튼에 없음 패스
        if int(nums[j]) in broken:
            break
        #고장난 숫자없이 마지막 자리까지 오면 비교후 최소 카운팅 갱신
        elif j == len(nums) - 1:
            #min (기존, (+,-) 클릭수 + 숫자 버튼클릭수)
            min_count = min(min_count, abs(int(nums) - target) + len(nums))

print(min_count)


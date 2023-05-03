#9095
import sys
input = sys.stdin.readline

# sol(1) : 1 , sol(2) : 2, sol(3) : 4 , sol(4) = sol(1)+sol(2)+sol(3)
def sol(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    elif n==3:
        return 4
    else :
        return sol(n-1)+sol(n-2)+sol(n-3)

T = int(input())
for i in range(T):
    n = int(input())
    print(sol(n))
import sys
input = sys.stdin.readline
L, C = map(int, input().split())
a = list(map(str, input().split()))
alphalist = sorted(a)
moeum = ['a','e','i','o','u']

ans = []
def findC(k):
    if len(ans) == L: #4개의 조합일때
        #print("there is 4")
        moeumcount = jaeumcount = 0
        for i in range(L):
            if ans[i] in moeum:
                moeumcount += 1
            else:
                jaeumcount += 1
        #모음 1개이상 자음 2개이상
        if moeumcount >=1 and jaeumcount >=2:
            print("".join(map(str, ans)))
        return
    for i in range(k,C):
        #print(i,k)
        if alphalist[i] not in ans: #중복확인
            ans.append(alphalist[i])
            #print(alphalist[i]+" appended" + str(i))
            k=i+1
            findC(k)
            ans.pop() #return하면 여기로 넘어옴

findC(0)


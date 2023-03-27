name = input()
result = 0

def findbeauty(a,b):
    beauty = 0
    for i in (range(b,a-1,-1)):
        if(name[a]!=name[i]):
            beauty=i-a
            break
    return beauty

k=0
for i in range(len(name)):
    for j in range(k,len(name)):
        result = result + findbeauty(i,j)
    k=k+1

print(result)
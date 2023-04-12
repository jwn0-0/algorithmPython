import itertools
dwarf = []
answer = []
#입력값 받기
for i in range(9):
    dwarf.append(int(input()))
#9개중 7개 조합으로 뽑아내기
for com in itertools.combinations(dwarf,7):
    if sum(com) == 100:
        answer = list(com)
        break
#sort 해서 print하기
answer.sort()
for i in answer:
    print(i)

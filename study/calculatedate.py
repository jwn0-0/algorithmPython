E, S, M = map(int, input().split())

EE=SS=MM=answer = 1
while True:
    if(E == EE and S == SS and M == MM):
        break
    #answer를 계속 1씩 높여주면서 카운트
    answer +=1
    EE += 1
    SS += 1
    MM += 1

    if(EE>=16): EE = EE-15
    if(SS>=29): SS = SS-28
    if(MM>=20): MM = MM-19

print(answer)
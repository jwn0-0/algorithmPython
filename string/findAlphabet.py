from string import ascii_lowercase

alpha = list(ascii_lowercase)
s = input()
output = []
for i in range(len(alpha)):
    count = 0
    for j in range(len(s)):
        if(alpha[i]==s[j]):
            output.append(j)
            break
        else:
            count += 1
    if(count==len(s)):
        output.append(-1)
#2가지 출력방법
print(*output)
print(' '.join(map(str,output)))


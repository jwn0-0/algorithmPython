
image = [[207, 207, 207, 84], [207, 207, 84, 255], [207, 84, 84, 207], [84, 255, 207, 0]]

n = len(image) #4
answer = []

for i in range(n):
    a = []
    for j in range(n):
        a.append(image[i][j])
    for j in range(n):
        a.append(image[i][3-j])
    answer.append(a)

for i in range(n):
    b=[]
    for j in range(n):
        b.append(image[3-i][j])
    for j in range(n):
        b.append(image[3-i][3-j])
    answer.append(b)

print(answer)


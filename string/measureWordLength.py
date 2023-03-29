import sys

#엔터 입력이 들어가기에 rstrip이용해서 엔터입력을 무시해줘야한다
a=list(map(str,sys.stdin.readline().rstrip("\n")))
print(len(a))
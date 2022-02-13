# 최대 최소 출력
n = int(input())
m = list(map(int,input().split()))
m.sort()
print(m[0],m[-1])


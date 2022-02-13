# 최대 최소 출력
# n = int(input())
# m = list(map(int,input().split()))
# m.sort()
# print(m[0],m[-1])

# 최댓값 및 위치 출력
n = []
for n in range(9):
    n.append(int(input()))
print(max(n), n.index(n) + 1)
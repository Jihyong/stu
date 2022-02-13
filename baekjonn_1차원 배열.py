# 최대 최소 출력
# n = int(input())
# m = list(map(int,input().split()))
# m.sort()
# print(m[0],m[-1])

# 최댓값 및 위치 출력
# n = []
# for i in range(9):
#     n.append(int(input()))
# print(max(n), n.index(max(n)) + 1)
# n = []
# for i in range(9):
#     n.append(int(input()))
# print(max(n), n.index(max(n))+1)

# 세자리 자연수의 곱 a * b * c의 결과값에 나온 각 숫자 개수 구하기
a = int(input())
b = int(input())
c = int(input())
result = list(str(a*b*c))
for i in range(10):
    print(result.count(str(i)))

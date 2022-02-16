# def solve(a):
#     number = 0
#     for i in a:
#         number += i
#         return number
# a = [40,60,90,80]
# result = solve(a)
# print(result)

# 셀프 넘버
natural_num = set(range(1,10001))
generated_num = set()

# for i in range(1,10001):
#     for j in str(i):
#         i += int(j)
#     generated_num.add(i)
# self_num = sorted(natural_num - generated_num)
# for i in self_num:
#     print(i)

# 한수
n = int(input())
hansu = 0
for i in range(1,n+1):
    if i < 100:
        hansu += 1
    else:
        n_str = list(map(int,str(i)))
        if n_str[2] - n_str[1] == n_str[1] - n_str[0]:
            hansu += 1
print(hansu)

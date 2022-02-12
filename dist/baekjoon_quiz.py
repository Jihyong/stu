#10952번
import sys
while True:
    a , b = map(int,sys.stdin.readline().split())
    if a == 0 and b == 0:
        break
    print(a + b)

#10951  # EOF (End of file 에 대한 예외처리 try ~ except~
while True:
    try:
        a,b = map(int,sys.stdin.readline().split())
        print(a + b)
    except:
        break
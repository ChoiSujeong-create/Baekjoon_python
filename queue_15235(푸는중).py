import queue
from sys import stdin
n = int(stdin.readline())
get_pizza = map(int, stdin.readline().split())
result = [0 for i in range(n)] # list 값을 0으로 초기화
cnt = 0
while(1):
    for i in range(n):
        if get_pizza[i] != 0:
            get_pizza[i] -= 1
            cnt += 1
            if get_pizza[i] == 0:
                result[i] = cnt

for i in range(n):
    print(result[i])

# 시간 줄이기
# deque 없이 풀기
# 파이썬의 리스트의 가장 앞 데이터를 쓰거나 지우면 리스트 내부의 전체 데이터를 다시 써주어야 하기 때문에 시간이 오래 걸린다.
# 따라서 가장 앞을 가르키는 인덱스 값을 이용함
from sys import stdin
n = int(stdin.readline())
list_queue = list()
f = 0
for i in range(n):
    cmd = stdin.readline().split()
    if cmd[0] == "push":
        list_queue.append(cmd[1])

    elif cmd[0] == "pop":
        if (len(list_queue)-f) == 0:
            print(-1)
        else:
            print(list_queue[f])
            f += 1
    elif cmd[0] == "size":
        print(len(list_queue)-f)

    elif cmd[0] == "empty":
        if (len(list_queue)-f) == 0:
            print(1)
        else:
            print(0)

    elif cmd[0] == "front":
        if (len(list_queue)-f) == 0:
            print(-1)
        else:
            print(list_queue[f])

    elif cmd[0] == "back":
        if (len(list_queue)-f) == 0:
            print(-1)
        else:
            print(list_queue[(len(list_queue)-1)])

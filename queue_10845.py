from sys import stdin
n = int(stdin.readline())
list_queue = list()
for i in range(n):
    cmd = stdin.readline().split()
    if cmd[0] == "push":
        list_queue.append(cmd[1])

    elif cmd[0] == "pop":
        if len(list_queue) == 0:
            print(-1)
        else:
            print(list_queue[0])
            del list_queue[0]

    elif cmd[0] == "size":
        print(len(list_queue))

    elif cmd[0] == "empty":
        if len(list_queue) == 0:
            print(1)
        else:
            print(0)

    elif cmd[0] == "front":
        if len(list_queue) == 0:
            print(-1)
        else:
            print(list_queue[0])

    elif cmd[0] == "back":
        if len(list_queue) == 0:
            print(-1)
        else:
            print(list_queue[(len(list_queue)-1)])

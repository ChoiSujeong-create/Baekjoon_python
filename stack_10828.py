from sys import stdin
n = int(stdin.readline())
list_stack = list()

for i in range(n):
    cmd = stdin.readline().split()
    if cmd[0] == "push":
        list_stack.append(int(cmd[1]))
    elif cmd[0] == "pop":
        if len(list_stack) == 0:
            print(-1)
        else:
            print(list_stack[-1])
            del list_stack[-1]
    elif cmd[0] == "size":
        print(len(list_stack))
    elif cmd[0] == "empty":
        if len(list_stack) == 0:
            print(1)
        else:
            print(0)
    elif cmd[0] == "top":
        if len(list_stack) == 0:
            print(-1)
        else:
            print(list_stack[-1])

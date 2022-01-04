from sys import stdin
n = int(stdin.readline())
result = []
num_arr = []
cnt = 1
no_message = True
for i in range(n):
    x = int(stdin.readline())
    while cnt <= x:  # cnt가 x보다 작을 때 까지 반복
        num_arr.append(cnt)  # num_arr에는 cnt값을 축적시킴
        result.append("+")  # result 에 + 추가
        cnt += 1  # cnt 하나씩 증가 시키기

    if num_arr[-1] == x:  # num_arr의 마지막 값과 x의 값이 같을 때
        num_arr.pop()  # num_arr의 마지막 값을 꺼내고
        result.append("-")  # result 에 - fmf cnrk
    else:  # num_arr 의 마지막 값과 x의 값이 다를 때
        no_message = False  # no_message에 False 저장
        # 여기서 끝내지 않는 이유는 반복문을 끝까지 실행하여 입력값을 전부 입력 받고 no를 출력 하기 때문

if no_message == False:
    print("NO")
else:
    for i in range(len(result)):
        print(result[i])

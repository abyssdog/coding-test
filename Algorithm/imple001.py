# 내가 푼것,  x, y 값으로 바로 계산함.
def solution():
    max = int(input())
    move = map(str, input().split())
    x, y = 1, 1
    for i in move:
        if i == 'L' and x - 1 > 1:
            y -= 1
        elif i == 'R' and x + 1 < max:
            y += 1
        elif i == 'U' and y - 1 > 1:
            x -= 1
        elif i == 'D' and y + 1 < max:
            x += 1
    print(f'{x} {y}')


# 해설 내가 if-elif 로 구현한 부분을
# 이동과 이동시 값의 변수를 배열로 구성하여
# 짜임새 있게 만들었음.
def solution1():
    n = int(input())
    x, y = 1, 1
    plans = input().split()

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    move_types = ['L', 'R', 'U', 'D']

    for plan in plans:
        for i in range(len(move_types)):
            if plan == move_types[i]:
                nx = x + dx[i]
                ny = y + dy[i]
        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue
        x, y = nx, ny
    print(f'{x} {y}')


solution()
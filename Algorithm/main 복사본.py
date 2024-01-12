def solution(n):
    res = [[0 for j in range(n)] for i in range(n)]
    my = [1, 0, -1, 0]
    mx = [0, 1, 0, -1]
    x, y = 0, 0
    idx = 0
    for i in range(1, n*n+1):
        res[x][y] = i
        nx = x + mx[idx]
        ny = y + my[idx]
        # 제일 중요한 부분. 아마 외곽 도는거는 가능하겠지만,
        # 내부의 충돌 감지는 맨끝의 res[nx][ny] 부분이 하게됨.
        if nx >= n or nx < 0 or ny >= n or ny < 0 or res[nx][ny] != 0:
            # 왼 오 위 아래를 이동하도록 세팅하는 부분.
            # 방향이 반시계로만 돌아서 가능함.
            idx = (idx + 1) % 4
            nx = x + mx[idx]
            ny = y + my[idx]
        x, y = nx, ny
    print(res)


solution(4)
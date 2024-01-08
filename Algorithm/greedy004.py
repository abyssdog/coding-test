import time


def solution():
    N, K = map(int, input().split())
    cnt = 0
    # N 이 1이 될때까지 반복해야함.
    while N != 1:
        # 각 과정마다 카운트를 해야하니 각 과정을 if문 하나로 묶기
        if N % K == 0:
            N //= K
        else:
            N -= 1
        cnt += 1
    print(cnt)


# 답안
def solution2():
    N, K = map(int, input().split())
    res = 0
    while True:
        # N == K 로 나누어 떨어지는 수가 될때까지 1씩 빼기
        target = (N // K) * K
        res += (N - target)
        N = target
        # N 이 K보다 작을 때 반복문 탈출
        if N < K:
            break
        # K 로 나누기
        res += 1
        N //= K
    res += (N-1)
    print(res)


st = time.time()
solution()
et = time.time()
elapsed_time = et - st
print(f"Elapsed Time: {elapsed_time:.6f} seconds")
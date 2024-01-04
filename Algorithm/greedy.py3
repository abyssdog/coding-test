def solution():
    N, M, K = 5, 8, 3
    arr = [2, 4, 5, 4, 6]
    # 입력 받은 수 정렬
    a = sorted(arr)
    # 가장 큰 수 2개만 선택
    f = a[len(a)-1]
    s = a[len(a)-2]
    answer = 0
    # 한번에 K만큼만 반복하기
    for i in range(1, M+1):
        if i % K == 0:
            answer += s
        else:
            answer += f
    print(answer)
    
solution()
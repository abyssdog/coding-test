
def solution(a, b, c, d):
    arr = [a, b, c, d]
    t = {}
    res = 0
    for i in arr:
        if i not in t:
            t[i] = 1
        else:
            t[i] += 1
    sa = sorted(t.items(), key=lambda a: a[1], reverse=True)
    for i in range(len(sa)):
        key = sa[i][0]
        val = sa[i][1]
        if val == 4:
            res = 1111 * key
        elif val == 3:
            res = (10 * key + sa[i+1][0]) ** 2
        elif val == 2 and sa[i+1][1] == 2:
            res = (key + sa[i+1][0]) * abs(key - sa[i+1][0])
        elif val == 2 and sa[i+1][1] == 1:
            res = sa[i+1][0] * sa[i+2][0]
        elif val == 1:
            res = sorted(t.items())[0][0]
        break
    print(res)
    # print(tarr)

solution(2, 2, 2, 2)
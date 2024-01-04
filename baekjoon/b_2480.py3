def check(ju):
    first = []
    dup = []
    count = 1
    for i in ju:
        if i not in first:
            first.append(i)
        else:
            dup.append(i)
            count += 1
    if len(first) == 3:
        sorted_nums = sorted(first)
        dup.append(sorted_nums[len(first)-1])
    return dup[0], count

def cal(nun, cnt):
    if cnt == 1:
        res = nun*100
    elif cnt == 2:
        res = 1000+nun*100
    elif cnt == 3:
        res = 10000+nun*1000
    return res

a = list(map(int, input().split()))
nun, cnt = check(a)
res = cal(nun, cnt)

print(f"{res}")
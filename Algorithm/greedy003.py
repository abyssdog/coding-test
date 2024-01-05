import time

# 0.000009 seconds
# def solution():
#     n, m = 2, 4
#     arr = [[7, 3, 1, 8], [3, 3, 3, 4]]
#     a = 0
#     for i in arr:
#         b = i[0]
#         for j in i:
#             if b > j:
#                 b = j
#         if a < b:
#             a = b
#     print(a)

# 0.000010 seconds
# def solution():
#     n, m = 2, 4
#     arr = [[7, 3, 1, 8], [3, 3, 3, 4]]
#     a = 0
#     for i in arr:
#         b = min(i)
#         if a < b:
#             a = b
#     print(a)

st = time.time()
solution()
et = time.time()
elapsed_time = et - st
print(f"Elapsed Time: {elapsed_time:.6f} seconds")
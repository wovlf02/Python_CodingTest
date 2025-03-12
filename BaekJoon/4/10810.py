n, m = map(int, input().split())
lst = [0]*n
for i in range(m):
    s, e, b = map(int, input().split())
    for j in range(s, e + 1):
        lst[j - 1] = b
for i in range(n):
    print(lst[i], end=" ")
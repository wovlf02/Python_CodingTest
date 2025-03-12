n, m = map(int, input().split())
lst = []
for i in range(0, n):
    lst.append(i + 1)
for i in range(m):
    a, b = map(int, input().split())
    temp = lst[a - 1]
    lst[a - 1] = lst[b - 1]
    lst[b - 1] = temp
for i in range(n):
    print(lst[i], end=" ")
lst = []
temp = []
n, m = map(int, input().split())
for i in range(n):
    lst.append(i + 1)
for i in range(m):
    a, b = map(int, input().split())
    temp = lst[a - 1:b]
    temp.reverse()
    lst[a - 1:b] = temp
for i in range(n):
    print(lst[i], end=' ')
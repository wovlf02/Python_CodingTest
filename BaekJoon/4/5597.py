lst = []
for i in range(1, 31):
    lst.append(i)
for i in range(28):
    a = int(input())
    lst.remove(a)
print(min(lst))
print(max(lst))
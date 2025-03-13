a = int(input())
lst = list(map(int, input().split()))
b = max(lst)
for i in range(a):
    lst[i] = lst[i] / b * 100
print(sum(lst) / a)
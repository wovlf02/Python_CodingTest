a, b = map(int, input().split())
if b - 45 >= 0:
    print("%d %d" % (a, (b - 45)))
else:
    a -= 1
    if a < 0:
        a = 23
        print("%d %d" % (a, (60 + (b - 45))))
    else:
        print("%d %d" % (a, (60 + (b - 45))))
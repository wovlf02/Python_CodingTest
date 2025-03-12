a, b, c = map(int, input().split())
if a == b and b == c and a == c:
    print("%d" % (10000 + (a * 1000)))
elif a == b and b != c:
    print("%d" % (1000 + (a * 100)))
elif b == c and a != c:
    print("%d" % (1000 + (b * 100)))
elif c == a and b != c:
    print("%d" % (1000 + (c * 100)))
else:
    if a > b and a > c:
        print("%d" % (a * 100))
    elif b > a and b > c:
        print("%d" % (b * 100))
    elif c > a and c > b:
        print("%d" % (c * 100))
while True:
    try:
        a, b = map(int, input().split())
        print("%d" % (a + b))
    except:
        break
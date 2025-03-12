import sys

a = int(sys.stdin.readline().rstrip())
for i in range(a):
    b, c = map(int, sys.stdin.readline().rstrip().split())
    print("%d" % (b+c))
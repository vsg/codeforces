a = {}
b = []
for _ in xrange(int(raw_input())):
    n, s = raw_input().split()
    if n in a:
        a[n] += int(s)
    else:
        a[n] = int(s)
    b += [(n, a[n])]
ms = max(a.values())
for n, s in b:
    if a[n] == ms and s >= ms:
        print n
        break

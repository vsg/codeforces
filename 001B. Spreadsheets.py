import re, string

def itoa(i):
    r = ''
    while i > 0:
        i, d = divmod(i-1, 26)
        r = string.uppercase[d] + r
    return r

def atoi(a):
    r = 0
    for c in a:
        r = 26 * r + string.uppercase.index(c) + 1
    return r

T = int(raw_input())
for t in xrange(T):
    line = raw_input()
    m = re.match("([A-Z]+)([0-9]+)([A-Z]+)?([0-9]+)?", line)
    if m.group(3) == 'C':
        r, c = m.group(2), itoa(int(m.group(4)))
        print c + r
    else:
        r, c = int(m.group(2)), atoi(m.group(1))
        print 'R%dC%d' % (r, c)


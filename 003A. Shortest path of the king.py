p = lambda x: (ord(x[0]), int(x[1]))
x0, y0 = p(raw_input())
x1, y1 = p(raw_input())

p = []
while (x0, y0) != (x1, y1):
    m = ''
    if x0 > x1: 
        m += 'L'
        x0 -= 1
    elif x0 < x1: 
        m += 'R'
        x0 += 1
    
    if y0 > y1: 
        m += 'D'
        y0 -= 1
    elif y0 < y1: 
        m += 'U'
        y0 += 1

    p += [m]

print len(p)
for x in p:
    print x

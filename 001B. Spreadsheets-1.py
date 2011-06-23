from string import uppercase

T = int(raw_input())
for t in xrange(T):
    line = raw_input()
    
    if line[0] == 'R' and line[1] not in uppercase:
        i = line.index('C')
        row = line[1:i]
        if i > 0:
            col = ''
            x = int(line[i+2:])
            while x > 0:
                x, d = divmod(x-1, 26)
                col = uppercase[d] + col
            print col + row
            continue
    col = 0
    for c in line:
        if c not in uppercase: break
        col = col*26 + uppercase.index(c) + 1
    print 'R%sC%d' % (row, col)
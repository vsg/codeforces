import re

def size(name):
    global d
    if len(d[name])==4:
        type, children, border, spacing = d[name]
        if not children:
            d[name] = (0, 0)
        else:
            ww, hh = zip(*map(size, children))
            b, s = 2 * border, spacing * (len(children) - 1)
            if type == 'VBox':
                d[name] = (b + max(ww), b + s + sum(hh))
            else:
                d[name] = (b + s + sum(ww), b + max(hh))
    return d[name]

d = {}
for _ in xrange(int(raw_input())):
    line = raw_input().strip()
    s = re.split("[ (,).]", line)
    if len(s)==5:
        type, name, width, height, _ = s
        d[name] = (int(width), int(height))
    elif len(s)==2:
        type, name = s
        d[name] = [type, [], 0, 0]
    else:
        name, op, arg, _ = s
        if op=='pack':
            d[name][1].append(arg)
        elif op=='set_border':
            d[name][2] = int(arg)
        elif op=='set_spacing':
            d[name][3] = int(arg)

for name in sorted(d):
    w, h = size(name)
    print name, w, h

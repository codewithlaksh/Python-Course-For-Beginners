l = [19, 20, 2, 3, 24, 19, 20, 89, 100, 120, 20]
d = {}

for i in l:
    # d[i] = l.count(i)
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

mx = max(d.values())

for i in l:
    if l.count(i) == mx:
        print(i, "has the maximum occurence!!")
        break
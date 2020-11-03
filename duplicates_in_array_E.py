def dup(s):
    d = {}
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    for x, y in d.items():
        if y > 1:
            print(x)


s = input()
dup(s)

if __name__ == "__main__":
    a = list(map(int, input().split()))
    f = 0
    l = len(a)-1
    while f < l:
        if a[f] > 0 and a[l] < 0:
            temp = a[f]
            a[f] = a[l]
            a[l] = temp
        elif a[f] < 0:
            f += 1
        elif a[l] > 0:
            l -= 1
    print(a)

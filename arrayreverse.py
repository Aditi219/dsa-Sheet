def rev(a, start, end):
    if start >= end:
        return
    a[start], a[end] = a[end], a[start]
    rev(a, start+1, end-1)


if __name__ == "__main__":
    n = input().split()
    l = len(n)
    rev(n, 0, l-1)
    print(n)

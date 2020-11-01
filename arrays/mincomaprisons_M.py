if __name__ == "__main__":
    n = list(map(int, input().split()))
    if len(n) % 2 == 0:
        if n[1] > n[0]:
            max1 = n[1]
            min1 = n[0]
        else:
            max1 = n[0]
            min1 = n[1]
        start = 2
    else:
        min1 = n[0]
        max1 = n[0]
        start = 1
    for i in range(start, len(n), 2):
        if n[i] > n[i+1]:
            if n[i] > max1:
                max1 = n[i]
            if n[i+1] < min1:
                min1 = n[i+1]
        else:
            if n[i+1] > max1:
                max1 = n[i+1]
            if n[i] < min1:
                min1 = n[i]
    print("Max : ", max1, " ", "Min : ", min1)

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    k = int(input())
    x = int(input())
    i = 0
    flag = 0
    while(i < len(arr)):
        if arr[i] == x:
            print(i)
            flag = 1
        diff = x-arr[i]
        i = i + max(1, int(abs(arr[i] - x) / k))
    if flag == 0:
        print("Not Present")

def spiral(matrix):
    arr = []
    if len(matrix) == 0:
        return arr
    m = len(matrix)
    n = len(matrix[0])
    k = 0
    l = 0
    i = 0
    while(k < m and l < n):
        for i in range(l, n):
            arr.append(matrix[k][i])
        k += 1
        for i in range(k, m):
            arr.append(matrix[i][n-1])
        n -= 1

        if k < m:
            for i in range(n-1, l-1, -1):
                arr.append(matrix[m-1][i])
            m -= 1

        if l < n:
            for i in range(m-1, k-1, -1):
                arr.append(matrix[i][l])
            l += 1
    print(arr)


if __name__ == "__main__":
    m, n = [int(x) for x in input().split()]
    matrix = []
    for i in range(m):
        l = list(map(int, input().split()))
        matrix.append(l)
    spiral(matrix)

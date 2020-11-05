
class job:
    def __init__(self, Id, deadline, profit):
        self.Id = Id
        self.deadline = deadline
        self.profit = profit


if __name__ == "__main__":
    test = int(input())
    for i in range(test):
        arr = []
        n = int(input())
        val = list(map(int, input().split()))
        for i in range(0, n*3, 3):
            arr.append(job(val[i], val[i+1], val[i+2]))
        arr.sort(key=lambda x: x.profit, reverse=True)
        res = [arr[0].profit]
        curr_deadline = arr[0].deadline
        d = {curr_deadline}
        for i in range(1, n):
            if arr[i].deadline == curr_deadline:
                continue
            if arr[i].deadline not in d:
                d.add(arr[i].deadline)
                curr_deadline = arr[i].deadline
                res.append(arr[i].profit)
        print(len(res), sum(res))

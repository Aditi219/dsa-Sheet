
class Activity:
    def __init__(self, start, finish, index):
        self.start = start
        self.finish = finish
        self.index = index


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        time = []
        n = int(input())
        s = list(map(int, input().split()))
        f = list(map(int, input().split()))
        for i in range(n):
            time.append(Activity(s[i], f[i], i))
        time.sort(key=lambda x: x.finish)
        # for i in range(n):
        #     print(time[i].start, time[i].finish)
        curr_end = time[0].finish
        res = [time[0].index+1]
        for i in range(1, n):
            if time[i].start >= curr_end:
                curr_end = time[i].finish
                res.append(time[i].index+1)
        print(" ".join(map(str, res)))

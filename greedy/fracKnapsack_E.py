class knapsack:
    def __init__(self, value, weight, cost):
        self.value = value
        self.weight = weight
        self.cost = cost


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        bag = []
        val = list(map(int, input().split()))
        w = list(map(int, input().split()))
        capacity = int(input())
        for i in range(len(val)):
            bag.append(knapsack(val[i], w[i], val[i]//w[i]))
        bag.sort(key=lambda x: x.cost, reverse=True)
        j = 0
        value = 0
        while capacity > 0:
            if bag[j].weight <= capacity:
                capacity -= bag[j].weight
                value += bag[j].value
                j += 1
            else:
                value += (bag[j].cost)*capacity
                capacity = 0
        print(value)
